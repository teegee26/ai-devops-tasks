# Simple database backup script in PowerShell

$DB_NAME = "app_database"
$BACKUP_DIR = "C:\var\backups\db"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = Join-Path $BACKUP_DIR "$DB_NAME" + "_$DATE.sql.gz"

# Check if the directory exists
if (-not (Test-Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR | Out-Null
    Write-Host "Created directory $BACKUP_DIR"
}

# Prompt for MySQL root password
$MySQLPassword = Read-Host -AsSecureString "Enter MySQL root password"
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($MySQLPassword)
$PlainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Perform the backup
Write-Host "Starting backup of $DB_NAME..."

$mysqldump = "mysqldump"
$gzip = "gzip"

$processInfo = New-Object System.Diagnostics.ProcessStartInfo
$processInfo.FileName = $mysqldump
$processInfo.Arguments = "-u root -p$PlainPassword $DB_NAME"
$processInfo.RedirectStandardOutput = $true
$processInfo.UseShellExecute = $false

$process = New-Object System.Diagnostics.Process
$process.StartInfo = $processInfo
$process.Start() | Out-Null

$gzipProcess = Start-Process -FilePath $gzip -ArgumentList @() -RedirectStandardInput $true -RedirectStandardOutput $true -NoNewWindow -PassThru

$process.StandardOutput.BaseStream.CopyTo($gzipProcess.StandardInput.BaseStream)
$gzipProcess.StandardInput.Close()

[System.IO.File]::WriteAllBytes($FILENAME, [System.IO.StreamReader]::new($gzipProcess.StandardOutput.BaseStream).ReadToEndBytes())

$process.WaitForExit()
$gzipProcess.WaitForExit()

if ($process.ExitCode -eq 0 -and $gzipProcess.ExitCode -eq 0) {
    Write-Host "Backup successful: $FILENAME"
} else {
    Write-Host "Backup failed!"
    exit 1
}