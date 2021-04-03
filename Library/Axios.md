# Axios

Axios는 브라우저와 Node.js를 위한 Promise API를 활용한 HTTP 비동기 통신 라이브러리다. fetch와 ajax처럼 비동기 통신을 위해 만들어졌고 앞서 말한 fetch와 ajax보다 더 보기 좋고 간결하게 코드를 작성할 수 있게 도와준다.

<br />
 
# Axios 설치

```jsx
// npm
$ npm install axios

// yarn
$ yarn add axios
```

<br />
 
# Axios 사용법

### Axios 호출

Axios을 사용하기 위해서는 먼저 호출을 해줘야 한다.

```jsx
// browser
import axios from "axios";

// node
const axios = require("axios");
```

<br />
 
### axios.create( [ config ] )

`create` 메소드를 이용해 인스턴스를 생성할 수 있습니다.

```jsx
const api = axios.create({
  baseURL: "url",
  params: {
    page: 10,
    name: "abc",
  },
});
```

<br />
 
### 인스턴스 메소드

인스턴스 모든 메소드는 config 설정이 가능하다.

```jsx
axios.get(url, { config });
axios.post(url, { data }, { config });
axios.put(url, { data }, { config });
axios.patch(url, { data }, { config });
axios.delete(url, { config });
axios.request(config);
axios.head(url, { config });
axios.options(url, { config });
axios.getUri(config);
```

<br />
 
### config 옵션

config 옵션으로 다양한 옵션들이 있습니다. 자주 쓰일 법한 옵션들 위주로 작성합니다.

- `url` 요청에 사용될 서버 URL입니다.
- `method` 요청 할 때 사용될 메소드입니다. ex) get, post
- `baseURL` URL 뒤의 파라미터가 필요할 경우 사용됩니다.
- `params` URL 매개 변수입니다. 객체 모양이여야 합니다.
- `headers` 서버에 전송될 사용자 정의 헤더입니다.

<br />
 
## 응답 정보

요청에 따른 응답 결과에는 다음과 같은 정보가 포함되어 있습니다.

- `data` 서버에서 제공 된 데이터입니다.
- `status` 서버 응답의 상태 코드입니다.
- `statusText` 서버 응답의 상태 메시지입니다.
- `headers` 서버가 응답의 헤더입니다.
- `config` axios에 설정된 config 입니다.
- `request` 응답을 생성한 요청
