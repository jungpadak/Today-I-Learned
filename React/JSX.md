## JSX란?

---

JSX는 자바스크립트의 확장 문법이며 XML과 매우 비슷하게 생겼습니다. JSX로 작성한 코드는 실행되기 전 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트 형태의 코드로 변환됩니다.

```javascript
function App() {
  return (
    <div>
      Hello
      <b>react</b>
    </div>
  );
}
```

이렇게 JSX로 작성된 코드를 일반 JS로 작성해보면

```javascript
function App() {
  return React.createElement("div", null, "Hello", React.createElement("b", null, "react"));
}
```

이런식으로 복잡하게 작성하게 됩니다. 이를 편하게 작성하기 위해 JSX를 사용합니다.

<br/ >

## JSX의 장점

---

### 1. 보기 쉽고 익숙하다

위에 JS로 작성한것과 JSX를 비교 해 보면 누가 봐도 JSX가 쉽고 가독성이 좋다는걸 알 수 있습니다. HTML와 매우 비슷해서 익숙하기까지 합니다.

### 2. 높은 활용도

JSX에서는 div나 span 같은 HTML 태그를 사용할 수 있을 뿐만 아니라 컴포넌트를 HTML 태그 쓰듯이 JSX 안에서 작성할 수 있습니다.

<br/ >

## JSX 문법

---

JSX는 편리한 문법이지만, 몇 가지 규칙을 준수해야 합니다.

### 감싸인 요소

컴포넌트에 여러 요소들이 있다면 이 요소들은 반드시 부모 요소 하나로 감싸야 합니다.

```javascript
function() {
	return (
    	<h1> 안녕하세요 </h1>
    	<p> 잘 보이시나요? </p>
    )
}
```

이런 식으로 감싸여진 요소가 없이 요소들이 따로 논다면 오류가 발생하게 됩니다.

```javascript
function() {
	return (
    	<div>
    		<h1> 안녕하세요 </h1>
    		<p> 잘 보이시나요? </p>
    	</div>
    )
}
```

이렇게 항상 부모 요소로 감싸둬야 합니다.

이런 방식을 사용해야 하는 이유는 Virtual DOM에서 컴포넌트의 변화를 감지해 낼 때 효율적으로 비교할 수 있도록 하나의 DOM 트리 구조로 이루어져야 한다는 규칙이 있기 때문입니다.

<br/ >

### JS 표현

JSX는 DOM 요소들을 렌더링 하는 기능 외에 JSX 안에서 자바스크립트 표현식을 사용 할 수 있습니다. 사용 방법은 JSX 내부에 { }로 감싸면 됩니다.

```javascript
function() {
	const name = 'React';

	return (
    	<h1>{ name } 안녕하세요! </h1>
    	<p> 잘 보이시나요? </p>
    )
}
```

이런식으로 { } 안에 변수를 넣으면 브라우저엔 `React 안녕하세요!`로 나오게 됩니다.

<br/ >

### if문 대신 조건부 연산자

JSX 내부에서는 if문을 사용하지 못합니다. 때문에 JSX 밖에서 if문을 사용하여 값을 만들어 사용하던가 { }안에 삼항 연산자를 이용하여야 합니다.

```javascript
function() {
	const name = "리액트";

	return (
    	<div>
    		{ name === "리액트" ? (<h1>맞습니다.</h1>) : (<h1>아닙니다.</h1>) }
    	</div>
    )
}
```

<br/ >

### AND 연산자( && )를 사용한 조건부 렌더링

개발을 하다 보면 특정 조건을 만족할 때 보여 주고, 만족하지 않을 때 아예 아무것도 렌더링하지 않아야 하는 상황이 있습니다. 이럴 때도 조건부 연산자를 통해 구현이 가능합니다.

```javascript
function() {
	const name = "리액트";

	return { name === "리액트" && <h1>맞습니다.</h1> }
}
```

AND 연산자는 전자가 true면 후자를 반환하고 false면 전자를 반환시킵니다.
위의 코드는 true이므로 후자가 반환되어 브라우저에 `맞습니다`가 나타나겠죠

<br/ >

### undefined를 렌더링하지 않기

리액트 컴포넌트에서는 undefined를 렌더링하는 상황을 만들면 오류가 발생하게 됩니다.

값이 undefined일 수도 있다면, OR( || ) 연산자를 이용하여 오류를 방지할 수 있습니다.

```javascript
function() {
	const name = undefined;

	return { name || <h1>undefined가 맞습니다.</h1> }
}
```

OR 연산자는 전자가 true면 전자를 반환하고 false면 후자를 반환시킵니다.
위의 코드는 undefined가 false로 인식되기 때문에 후자가 반환됩니다.

<br/ >

### 인라인 스타일링

리액트에서 스타일을 적용할 때는 객체 형태로 작성해야 합니다. 주의 할 점은 font-size 같은 - 문자가 포함되어 있는 속성은 -를 떼고 카멜 표기법으로 표기해줘야 합니다. ex) fontSize, backgroundColor

```javascript
function() {
	const name = '리액트';
	const style = {
      width: '100px',
      height: '100px',
      fontSize: '16p',
      backgroundColor: 'blue'
    }

	return <div style={style}> {name} </div>
}
```

이런 식으로 인라인 스타일링을 줄 수 있습니다.

<br/ >

### class 대신 className

JSX에선 class가 아닌 className으로 사용해야합니다.

```javascript
function() {
	return (
    	<div>
    		<h1 className="hi"> 안녕하세요 </h1>
    		<p> 잘 보이시나요? </p>
    	</div>
    )
}
```

<br/ >

### 태그는 꼭 닫아야한다

HTML 코드를 작성할 때는 태그를 닫지 않아도 문제없이 작동하지만 JSX는 태그가 항상 닫혀 있어야 합니다. `<input></input>` 같이 태그 안에 내용이 들어가지 않는 경우엔 `<input />` 이렇게 작성도 가능합니다. 이를 self-closing이라 부릅니다.

<br/ >

### 주석

JSX 안에서의 주석은 자바스크립트에서의 주석과는 조금 차별점이 있습니다.
자바스크립트의 주석처럼 //, /\*\*/를 바로 입력하게 되면 브라우저에 표시가 됩니다
JSX 안에서의 주석은 항상 { } 안에 적어야합니다.
