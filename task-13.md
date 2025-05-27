```js
/**
 * Fetches user data from the API for a given user ID.
 *
 * @param {string|number} userId - The unique identifier of the user.
 * @returns {Promise<{name: string, email: string, lastLogin: Date} | null>} 
 *   A promise that resolves to an object containing the user's name, email, and last login date,
 *   or null if an error occurs.
 */
function fetchUserData(userId) {
    return fetch(`https://api.example.com/users/${userId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            return {
                name: data.name,
                email: data.email,
                lastLogin: new Date(data.lastLoginTimestamp)
            };
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return null;
        });
}
```