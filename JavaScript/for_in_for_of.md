# for in for out

자바스크립트엔 for문과 while문 외에도 여러가지 반복문이 있습니다. ES6에는 대상의 요소를 순회하기 위해 `for in`과 `for out`이라는 문법을 추가하였습니다. 이 문법 이름도 비슷하고 사용 방법도 비슷해 조금 헷갈려 둘의 차이점과 사용법을 간단하게 비교해보려 합니다.

<br />

## for in

`for in` 반복문은 객체를 프로퍼티의 수 만큼 순회하며 프로퍼티의 key값에 접근합니다. value 값에 접근하는 방법은 따로 없지만 주어진 key 값으로 value에 접근이 가능합니다. 자바스크립트 객체 속성엔 숨겨진 속성들이 있습니다. 그 중 하나가 `[[Enumerable]]` 이며 기본적으로 `true`로 지정되어 있습니다. 이러한 속성들을 열거형 속성이라 부르고 `for in`문은 프로퍼티가 열거형 속성이여야 사용이 가능합니다.

```jsx
const obj = {
  a: 1,
  b: 2,
  c: 3,
  d: 4,
};

for (let key in obj) {
  console.log(`${key} - ${obj[key]}`);
}

// a - 1
// b - 2
// c - 3
// d - 4
```

자바스크립트에선 배열도 객체이므로 for in을 사용 할 수 있습니다. 다만 해당 요소를 가져오는것이 아닌 index를 반환합니다.

```jsx
const arr = [10, 20, 30, 40];

for (let key in arr) {
  console.log(`${key} - ${arr[key]}`);
}

// 0 - 10
// 1 - 20
// 2 - 30
// 3 - 40
```

자바스크립트엔 배열도 종류가 있습니다 위와 같은 보통의 `Array`와 문자열과 Nodelist 같은 유사 배열 `ArrayLike`가 있죠 이런 유사 배열도 `for in`문을 사용 할 수 있습니다.

```jsx
const str = "abc";

for (let key in str) {
  console.log(`${key} - ${str[key]}`);
}

// 0 - a
// 1 - b
// 2 - c

const HTMLCollection = document.body.children;
// body 안엔 h1, span, div 태그가 있다 가정하겠습니다.

for (let key in HTMLCollection) {
  console.log(`${key} - ${HTMLCollection[key]}`);
}

// 0 - <h1>...</h1>
// 1 - <span>...</span>
// 2 - <div>...</div>

const arg = function () {
  return arguments;
};

for (let key in arg(9, 8, 7)) {
  console.log(key);
}

// 0
// 1
// 2
```

<br />
 
## for of

`for of`문은 반복할 수 있는 객체인 `iterable object`를 순회할 수 있도록 도와주는 반복문 입니다. 대표적인 이터러블 객체를 뽑자면 배열과 문자열이 있습니다. 또한 직접 Symbol.iterator라는 심볼을 이용해서 대상자를 이터러블 객체로 만들어 줄 수도 있습니다.

`for of`문은 루프마다 열거할 수 있는 프로퍼티, 요소의 수만큼 반복을 돌며 해당 프로퍼티, 요소에 접근합니다.

```jsx
const arr = [7, 8, 9];

for (let val of arr) {
  console.log(val);
}

// 7
// 8
// 9

const str = "Woogie";

for (let val of str) {
  console.log(val);
}

// W
// o
// o
// g
// i
// e
```

<br />
 
## for in / for of 차이점??

둘의 차이를 간단히 요약하자면

> for in : 객체의 열거 가능한 프로퍼티를 반복해 key를 반환

> for of : `iterabla.object`인 객체 즉, 배열에 요소만큼 반복해 요소를 반환

<br />
 
# 잡설

for in of in of 계속 볼때마다 이게 배열에 쓰던건가? 객체에 쓰던건가 헷갈리며 mdn의 도움을 받았는데 이렇게 정리해보니 둘의 차이점을 명확하게 알 수 있었다. 솔직히 `iterable`이라 던지 `iterator`이라던지 `[[Enumerable]]` 이러한 개념들은 정확하게 이해하진 못했다. 이는 나중에 따로 정리해보자!
