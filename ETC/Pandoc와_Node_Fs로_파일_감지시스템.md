# Pandoce과 Node Fs로 파일 감지 기능을 만들어보자

깃블로그를 만들어보려 하는데 마크다운이 익숙하고 보기도 편해서 마크다운을 이용해 블로그를 만들어보자라는 생각이 들었다. 그래서 마크다운 파일을 HTML로 변환하는 방법을 찾다가 발견한 Pandoc과 Fs를 기록해보려한다.

## Pandoc

[Pandoc Link](https://pandoc.org/index.html)

[Pandoc 변환 예제](https://www.lesstif.com/software-architect/pandoc-markdown-26083394.html)

Haskell 로 만들어진 문서 변환 작업프로그램으로 markdown, MediaWiki, texile, HTML, ms word, epub, PDF등으로 양방향 혹은 단반향으로 변환이 가능한 프로그램이다

### 설치

W**indow**

```jsx
$ choco install pandoc
```

윈도우는 choco로 설치해야한다.

**Ubuntu**

```jsx
$ sudo install pandoc
```

### 예제

pandoc도 엄청 많은 기능들이 있지만 지금 당장 내가 필요한것들만 적어두겠다.

**파일 변환**

```jsx
$ pandoc 파일명 -f 확장자 -t 확장자 -s -o 파일명
```

기본적인 구성은 이렇게 되어있다. 하나하나 뜯어보자면

**파일명** 변환시킬 대상을 루트와 함께 입력

**-f** from의 약자로 변환시킬 파일의 확장자를 입력한다.

**-t** to의 약자로 변환 시킨 파일의 확장자를 적는다

-**s** standalone의 약자이다.

**-o** 아웃풋의 약자이다 변환 시킨 파일의 루트와 함께 입력한다.

```jsx
$ pandoc ./test.md -f markdown -t html -s -o ./tset.html
```

이외에도 많은 기능들이 있는데 위에 링크에 가서 확인해보길 바란다.

html으로 변환할때 css 파일도 넣어줄 수 있다.

```jsx
$ pandoc 파일명 -f markdown -t html -c ex.css -s -o 파일명
```

**-c** css의 파일을 넣을수 있다. 여러개를 넣고 싶으면 여러번 입력하면 된다

```jsx
$ pandoc 파일명 -f markdown -t html -c ex.css -c a.css -s -o 파일명
```

## Node Fs

[Node Fs Link](https://nodejs.org/api/fs.html)

[Node Fs 생활코딩](https://opentutorials.org/module/938/7373)

Fs는 File System의 약자이다. Fs는 파일은 파일 처리에 관련된 모듈입니다. doc를 보면 엄청난 메소드들이 있다.

Node Fs는 따로 설치 할 필요 없이 Node에서 제공해주는 메소드이기 때문에 Node가 있다면 그냥 사용가능하다

```jsx
// 대신 fs를 불러와야한다.
const fs = require("fs");
```

### 예제

대강 내가 사용하려는 기능들만 적어두려한다.

**파일 변화 감지**

원하는 폴더 or 파일에 변화가 감지되면 바로 캐치해주는 기능이다.

```jsx
fs.watch("./", function (event, filename) {
  console.log("event: " + event);

  if (filename) {
    console.log("filename: " + filename);
  } else {
    console.log("error");
  }
});
```

```jsx
// 결과
$ event: change
$ filename: test.js
```

터미널에서 js 실행시키면 위와 같은 결과가 나온다.

**파일 읽기**

원하는 파일의 내용을 가져온다. md html js 종류를 가리지않고 그 안에 있는 모든걸 가져온다.

```jsx
// text.txt
안녕하세요 테스트에요
잘 되죠?
```

```jsx
fs.readFile("text.txt", "utf8", function (err, data) {
  console.log(data);
});
```

```jsx
// 결과
$ 안녕하세요 테스트에요
$ 잘 되죠?
```

**파일 쓰기**

원하는 파일 안에 데이터를 넣어줄 수 있다. html에 태그를 넣을수도 js에 코드를 넣을수도 있다.

```jsx
var data = "들어갑니다";

fs.writeFile("text.txt", data, "utf8", function (err) {
  console.log(" 완료");
});
```

```jsx
// text.txt
안녕하세요 테스트에요
잘 되죠?
들어갑니다
```

## Pandoc와 Fs의 시너지

Pandoc은 Markdown파일을 원하는 파일로 변환시켜준다. 그렇게 되면 Fs가 폴더내 변화를 감지하고 원하는 로직을 작성해서 파일의 내용을 뽑아 오거나 다른 파일에 내용을 넣어주거나 여러가지 기능을 만들수 있다.

같은 루트내에 이러한 파일들이 있다.

```html
// index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <!--Here-->
  </body>
</html>
```

```markdown
// test.md

# 안녕하세요

저는 `Woogie`입니다.

- 다들 행복하세요

1. 하하하 이거 쓰기 힘들다
```

나는 md파일을 html파일로 변환하고 그걸 감지해서 index.html에 링크 태그를 넣으려한다.

```js
const fs = require("fs");

const fileSystem = (root, to) => {
  let fileName = "";
  let aTag = "";
  let toggle = false;

  fs.watch(root, function (event, filename) {
    if (filename) {
      let indexOf = filename.indexOf(".");
      let fileFormat = filename.slice(indexOf + 1, filename.length);

      if (fileFormat === "html") {
        toggle = true;
        fileName = filename;
      }
    } else {
      console.log("error");
    }
  });

  setInterval(() => {
    console.log("No Sensing");
    if (toggle === true) {
      console.log("Read And Write");

      fs.readFile(`${to}`, "utf8", function (err, data) {
        aTag = `<a href=${root}${fileName}>${fileName}</a>`;
        let aTagReplace = data.replace(`<!--Here-->`, aTag);

        fs.writeFile(`${to}`, aTagReplace, "utf8", function (err) {});
      });

      toggle = false;
      console.log("End");
    }
  }, 2000);
};

fileSystem("./", "index.html");
```

위와 같은 로직을 실행하면 아래와 같이 index.html이 바뀐다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
	  <a href=./test.html>test.html</a> // 바뀜!!!!
  </body>
</html>
```

멋지다! 근데 이걸 블로그 만들때 어떻게 활용해야 할지 더 생각해봐야겠다.
