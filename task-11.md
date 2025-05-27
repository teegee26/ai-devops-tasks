## What is Jest?

[Jest](https://jestjs.io/) is a popular JavaScript testing framework maintained by Meta. It is used to write and run unit tests for JavaScript and TypeScript code, making it easier to ensure your code works as expected.

## How to Install Jest

1. Initialize your project (if you haven't already):

	```bash
	npm init -y
	```

2. Install Jest as a development dependency:

	```bash
	npm install --save-dev jest
	```

3. (Optional) Add a test script to your `package.json`:

	```json
	"scripts": {
	  "test": "jest"
	}
	```

## Writing a Unit Test for `sum`

Suppose your `sum` function is in a file called `sum.js`:

```js
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```

Create a test file named `sum.test.js`:

```js
// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

## Running the Test

Run the following command in your terminal:

```bash
npm test
```

or, if you didn't add the script:

```bash
npx jest
```

## Example Project Structure

```
your-project/
├── node_modules/
├── package.json
├── sum.js
└── sum.test.js
```