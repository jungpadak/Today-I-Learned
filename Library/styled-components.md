# styled-components

styled-components는 JS와 CSS파일을 따로 분리하여 관리하는 방식에서 벗어나 JS 파일 내에서 CSS를 사용할 수 있는 방식인 CSS in JS 방식을 이용함으로써 JS 코드 내에서 일반 CSS로 스타일을 입힐 수 있습니다.

보통 리액트와 많이 사용되는 라이브러리이고 리액트 컴포넌트를 쉽게 스타일링할 수 있다는 장점이 있습니다.

<br />
 
# 설치

```json
$ npm install --save styled-components
```

<br />
 
# 기본 문법

styled-components의 사용법은 아주 간단합니다. 라이브러리에서 styled를 불러와 사용 할 태그 or 컴포넌트를 작성해주고 일반적인 CSS 문법을 이용하여 스타일링하면 됩니다.

```jsx
const 커스텀된 컴포넌트 이름 = styled.태그`css...`
```

```jsx
import styled from "styled-components";

const Container = styled.div` css... `;
```

여기서 사용될 수 있는 태그는 HTML 태그를 넘어서 리액트에서 새롭게 만든 컴포넌트나 라이브러리에서 가져온 컴포넌트들도 모두 사용이 가능합니다. 이를 extend라고 부르며 이때는 `styled(컴포넌트)`형태로 작성해야 합니다.

```jsx
const Title = styled.h1` css... `;
const Link = styled(Link)` css... `;
const CustomApp = styled(App)`- css... `;
```

<br />
 
# 상태에 따른 CSS 변화

styled-components이 가장 큰 장점이라고 뽑으라면 상태에 따라 css를 바꿀 수 있다는 점을 뽑겠습니다. props로 전달 받은 상태에 따라 다른 스타일을 적용시킬 수 있는 기능을 제공하고 있습니다. 사용법은 간단하게 템플릿 리터럴이라는 점을 이용하여 `${}` 안에 원하는 로직을 작성할 수 있습니다.

```jsx
const Container = styled.div`
  width: 100%;
  height: 100vh;
  background-color: ${(props) => (props.color === "blak" ? "black" : "white")};
`;

const Component = ({ color }) => {
  return <Container color={color} />;
};
```

styled-components로 만들어진 커스텀 컴포넌트에 props를 전달 시키기 위해 보통의 컴포넌트들과 같은 방식으로 props를 전달 시킬 수 있습니다.

단순히 하나의 속성만 바꿀 수 있는게 아니라 여러개의 css 속성을 묶어서 정의할 수도 있습니다. 예를 들어 props로 넘어온 toggle이 true일때 크기를 절반 줄이고 싶다면 아래와 같이 작성할 수 있습니다.

```jsx
const Container = styled.div`
  width: 100%;
  height: 100vh;

  ${(props) =>
    props.toggle &&
    css`
      width: 50%;
      height: 50vh;
    `}
`;

const Component = ({ toggle }) => {
  return <Container toggle={toggle} />;
};
```

<br />
 
# Nesting

일반 CSS와 SASS의 가장 큰 차이는 nesting 기능의 유무입니다. styled-components도 SASS 처럼 nesting 기능을 제공해줌으로서 SASS와 비슷하게 작성하실 수 있습니다.

```jsx
const Container = styled.div`
  width: 100%;
  height: 100vh;
  background-color: #000;

  &:hover {
    background-color: #fff;
  }
`;
```

<br />
 
# Global style

모든 컴포넌트에 동일한 스타일을 입히거나 최상위에서 관리해야 하는 속성들을 global style을 이용해 관리할 수 있습니다. styled-components에는 두 가지의 global style이 있습니다. 브라우저의 기본 CSS 속성을 초기화 시켜주는 목적으로 사용되는 Globalstyle과 어느 컴포넌트에서도 사용할 수 있는 공통된 CSS를 모아둔 Thema가 있습니다.

각각의 파일을 만들어 관리하고 index.js에서 불러와 사용합니다.

```jsx
// Global.js
* {
	margin: 0;
	pdding: 0;
}

// Thema.js
const MainColor = styled.div`
	color: #000
`

// index.js
import { ThemaProvider } from 'styled-components'
import GlobalStyle from './style/global'
import thema from './style/thema'

ReatDOM.render(
	<React.StrictMode>
		<ThemaProvider thema={thema}>
			<App />
			<Global />
		</ThemaProvider>
	</React.StrictMode>
)

// 하위 컴포넌트에서 Thema 사용
const MainText = styled.div`
	color: ${props => props.thema.MainColor}
`
```
