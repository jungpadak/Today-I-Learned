# Global CSS 설정

리액트로 스타일 작업을 할 때 어플리케이션 전체에 적용하고 싶은 속성들이 생길 수 있습니다. 브라우저의 기본 css 속성들을 초기화 시키기 위한 reset css 처럼 전역에서 css를 관리하려면 styled-components의 GlobalStyle을 이용하면 되고 자주 쓰이는 색상, 크기와 같은 속성의 값들을 최상위에서 관리하고 필요할 때 마다 어느 곳에서든 사용이 가능한 Theme가 있습니다.

<br />
 
## GlobalStyle 사용법

GlobalStyle는 styled-components의 속성이므로 해당 라이브러리를 설치해야 합니다.

```css
$ npm install styled-components
```

사용 방법은 간단합니다. Global하게 스타일을 지정해 주기 위해 GlobalStyle이라는 파일을 하나 만들어서 styled-components의 createGlobalStyle을 불러와 css를 작성하면 됩니다.

```jsx
// GlobalStyle
import { createGlobalStyle } from "styled-components";
import { reset } from "styled-reset";

export const GlobalStyle = createGlobalStyle`
    ${reset}
`;

// App.js
import React from "react";
import { GlobalStyle } from "./style/global";

function App() {
  return (
    <>
      <GlobalStyle />
      <Home />
    </>
  );
}
```

작성된 GlobalStyle을 적용하기 위해서 최상위 컴포넌트인 App.js로 이동해 import로 GlobalStyle을 가져오고 App의 첫번째 컴포넌트로 GlobalStyle을 넣어주면 그 아래의 컴포넌트에 모두 적용이 됩니다.

여기서 styled-reset 라이브러리는 누군가 정의해둔 reset 속성들을 가져와 사용하는 겁니다.

<br />
 
## Theme 사용법

Theme도 GlobalStyle과 마찬가지로 styled-components 라이브러리의 속성이므로 설치가 필요하고 속성들을 관리하기 위한 Theme 파일을 하나 만들어 자주 쓰이는 속성들을 모아둡시다.

```jsx
// Theme.js
const fontSizes = {
	small: `14px`,
	base: `16px`,
	lg: `18px`
}

const colors = {
	logo: `#343411`,
	text: `#999`
}

// 자주 사용되는 스타일 속성들
const common = {
	flexCenter: `
		display: flex;
		justify-contents: center;
		align-items: center;
	`
	positionCenter: `
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	`
}

const theme = {
	fontSizes,
	colors,
	commo,
}

export default theme
```

이렇게 모아둔 속성드을 최상위 컴포넌트인 App.js에서 호출하여 사용하면 됩니다. 사용할 때는 styled-components의 ThemeProvider를 불러와 Theme를 적용 시킬 컴포넌트들을 ThemeProvider로 묶어주시면 됩니다. 이때 ThemeProvider의 theme 속성을 이용해 theme파일을 적용 시킬 수 있습니다.

```jsx
// App.js
import React from "react";
import { ThemeProvider } from "styled-components";
import theme from "./style/theme";
import { GlobalStyle } from "./style/global";

function App() {
  return (
    <ThemeProvider theme={thema}>
      <GlobalStyle />
      <Home />
    </ThemeProvider>
  );
}

export default App;
```

Theme가 적용된 하위 컴포넌트에서 어떻게 Theme를 이용하는지 알아보겠습니다.

```jsx
// Home.js

import React from "react";
import styled from "styled-components";

const Container = styled.div`
  ${({ theme }) => theme.common.flexCenter}
  width: 500px;
  height: 500px;
  background-color: ${({ theme }) => theme.colors.logo};
`;

function Home() {
  return (
    <>
      <Container />
    </>
  );
}

export default Home;
```

ThemeProvider 안에 있는 컴포넌트들은 props로 theme를 받아 오므로 위의 코드대로 작성하여 사용하면 됩니다.
