자바스크립트에 내장된 고차 함수 `Reduce`는 정말 다양한 방법으로 활용이 가능합니다. `Reduce`를 배울때 단순하게 숫자의 합을 구하는 예제를 자주 사용하는데요 이런 단순한 활용말고도 다양한 활용법들을 정리해볼까 합니다.

### 배열에서 중복된 요소 카운팅

```jsx
let arr = ["code", "states", "code", "wewin", "pre", "code", "pre"];

let arrReduce = arr.reduce((a, c) => {
  if (a[c]) a[c]++;
  else a[c] = 1;

  return a;
}, {});

console.log(arrReduce); // {code: 3, states: 1, wewin: 1, pre: 2}
```

위와 같이 `Reduce`로 간단하게 중복된 요소의 갯수를 구해낼 수 있습니다.

### 배열에서 중복된 요소 제거

```jsx
let arr = ["code", "states", "code", "wewin", "pre", "code", "pre"];

let arrReduce = arr.reduce((a, c) => {
  return a.indexOf(c) === -1 ? [...a, c] : a;
}, []);

consoel.log(arrReduce); // ["code", "states", "wewin", "pre"]
```

Set 메소드가 따로 있긴하지만 Reduce로도 배열의 중복된 요소를 제거할 수도 있습니다.

### 객체 원하는 값 다루기

```jsx
let users = [
  { name: "woogie", age: "13" },
  { name: "kakao", age: "7" },
  { name: "naver", age: "20" },
  { name: "line", age: "7" },
  { name: "baemin", age: "20" },
];

let ageFilter = users.reduce((a, c) => {
  if (a[c.age]) a[c.age].push(c.name);
  else a[c.age] = [c.name];

  return { ...a };
}, {});

console.log(ageFilter);

// {
//  7: ['kakao','line']
//  13: ['woogie']
//  20: ['naver', 'baemin']
// }
```

유저 데이터를 담은 객체에서 나이별로 유저의 이름을 모아주는 로직을 reduce로 만들 수 있습니다.

```jsx
let users = [
  { id: 401, name: "kakao" },
  { id: 142, name: "baemin" },
  { id: 754, name: "naver" },
  { id: 231, name: "line" },
];

let idFilter = users.reduce((a, c) => {
  return { ...a, [c.id]: c };
}, {});

console.log(idFilter);

//  {
//   142: {id: 142, name: 'baemin'},
//   231: {id: 231, name: 'line'},
//   401: {id: 401, name: 'kakao'},
//   754: {id: 754, name: 'naver'}
//  }
```

이렇게 id를 밖으로 꺼내준다면 id를 찾을때 쓸데없이 순회 할 필요없이 `idFilter[142].name` 이러한 방식으로 빠른 시간내에 찾을 수 있다.

### 이차원 배열 풀어주기

```jsx
let arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

let arrSpread = arr.reduce((a, c) => {
  return [...a, ...c];
}, []);

console.log(arrSpread); // [1,2,3,4,5,6,7,8,9]
```

이차원 배열을 간단하게 이어 붙이는 로직을 reduce로도 만들 수 있습니다.

## 끝

이 외에도 더 다양하게 활용 가능하겠지만 아직 내 머리론 여기까지가 한계인듯하다. 개인적으로 reduce를 잘쓰면 뭔가 멋있어 보인다고 해야하나? 효율도 중요하겠지만 그냥 재밋다.
