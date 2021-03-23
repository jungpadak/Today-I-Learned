## Express

Express는 Node.js를 빠르고 간결하게 사용하기 위해 만들어진 웹 프레임워크입니다.

<br />
 
## Express 설치

```jsx
$ npm install express --save
```

<br />
 
## Express 사용

```jsx
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

위와 같은 코드를 적고 터미널에서 실행 시키면 `Hello World`가 출력 된다.

<br />
 
## 기본 라우팅

### Get

```jsx
app.get("/", function (req, res) {
  res.send("Hello World!");
});
```

### Post

```jsx
app.post("/", function (req, res) {
  res.send("Got a POST request");
});
```

### Put

```jsx
app.put("/user", function (req, res) {
  res.send("Got a PUT request at /user");
});
```

### Delete

```jsx
app.delete("/user", function (req, res) {
  res.send("Got a DELETE request at /user");
});
```

<br />
 
## 라우팅

### route()

route()를 이용하면 라우트 경로에 대하여 체인 가능한 라우트 핸들러를 작성할 수 있습니다. 경로는 한 곳에 지정되어 있으므로, 모듈식 라우트를 작성하면 중복성과 오타가 감소하여 도움이 됩니다.

```jsx
app
  .route("/book")
  .get(function (req, res) {
    res.send("Get a random book");
  })
  .post(function (req, res) {
    res.send("Add a book");
  })
  .put(function (req, res) {
    res.send("Update the book");
  });
```

### express.Router

`express.Router` 클래스를 사용하면 모듈식 마운팅 가능한 핸들러를 작성할 수 있습니다. `Router` 인스턴스는 완전한 미들웨어이자 라우팅 시스템이며, 따라서 “미니 앱(mini-app)”이라고 불리는 경우가 많습니다.

다음 예에서는 라우터를 모듈로서 작성하고, 라우터 모듈에서 미들웨어 함수를 로드하고, 몇몇 라우트를 정의하고, 기본 앱의 한 경로에 라우터 모듈을 마운트합니다.

다음의 내용이 입력된 `birds.js`라는 이름의 라우터 파일을 앱 디렉토리에 작성하십시오.

```jsx
var express = require("express");
var router = express.Router();

// middleware that is specific to this router
router.use(function timeLog(req, res, next) {
  console.log("Time: ", Date.now());
  next();
});
// define the home page route
router.get("/", function (req, res) {
  res.send("Birds home page");
});
// define the about route
router.get("/about", function (req, res) {
  res.send("About birds");
});

module.exports = router;
```

이후 앱 내에서 다음과 같이 라우터 모듈을 로드하십시오.

```jsx
var birds = require('./birds');
...
app.use('/birds', birds);
```
