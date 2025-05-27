function getEnvironmentConfig(env) {
    const configs = {
        development: {
            apiUrl: 'http://localhost:3000/api',
            debug: true,
            timeout: 5000
        },
        testing: {
            apiUrl: 'http://test-server:3000/api',
            debug: true,
            timeout: 5000
        },
        staging: {
            apiUrl: 'https://staging.example.com/api',
            debug: false,
            timeout: 10000
        },
        production: {
            apiUrl: 'https://api.example.com',
            debug: false,
            timeout: 15000
        }
    };

    // Default to 'development' config if env is unknown
    return configs[env] || configs.development;
}