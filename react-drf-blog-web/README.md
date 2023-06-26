# React DRF Blog Frontend

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

## Requirements

- Node.js v18.16.1
- npm v9.5.1
- Google analytics tracking ID
- A public github repository for saving comments
  - need to install Utterances (https://github.com/apps/utterances)

## Setup

To get started with using DRF Blog, run the following steps:

#### 1. Install packages

```bash
$ npm install
```

#### 2. Edit .env.development file

```
# Backend API URL
REACT_APP_API_URL=http://localhost:8000

# Google analytics tracking ID
REACT_APP_GOOGLE_ANALYTICS_TRACKING_ID=G-XXXXXXXXXX

# Github public repository url
REACT_APP_UTTERANCES_COMMENT_GITHUB_URL=username/repo-name
```

#### 3. Run

```bash
$ npm run start
```

## License

Licensed under the
[MIT](https://github.com/kimfame/react-drf-blog/blob/main/react-drf-blog-web/LICENSE) License.
