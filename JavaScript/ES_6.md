# ECMAScript 6

ECMAScript는 Ecma 인터내셔널에 의해 제정 된 ECMA-262라는 기술 규격에 의해 정의된 범용 스크립트 언어입니다. Javascript는 ECMAScript의 사양을 준수하고 그 중 ECMAScipt 6는 2015년에 새롭게 개선 된 버전이며 현재는 ECMASctipt 11까지 나온 상태입니다. ECMAScript 6에서는 유용하고 코드를 간결하게 해주는 좋은 기능들이 추가되어 자주 사용하는 기능들에 대해 작성합니다.

<br />
 
## Let / Const

`let`과 `const` 는 변수를 선언하는 새로운 키워드입니다. `var`와 다른 점이 존재하는데요 `var` 의 스코프 범위는 외부 함수까지 침범하지만 `let`과 `const`는 블록 레벨 스코프를 지원하고 있어 블록 문 만큼의 스코프 범위를 가집니다. 그리고 `const`는 한번 선언과 할당이 이뤄지면 더 이상 재 선언과 재 할당이 불가능합니다.

```jsx
// es5
var es5 = 10;

if (true) {
  var es5 = 20;
}

console.log(es5); // 20

// es6 - let
let es6Let = 10;

if (true) {
  let es6Let = 20;
}

console.log(es6Let); // 10

// es6 - const
const es6Const = 10;
const es6Const = 20; // TypeError: Assignment to constant variable
```

<br />
 
## Arrows Function

Arrows Function은 말 그대로 화살표 함수입니다. 기존의 함수를 `=>`의 형태로 축약 시키는 방법이죠 이 Arrows Function은 무조건 함수 선언식으로 사용해야 합니다.

```jsx
// es5
function Fn() {...}
const Fn = function() {...}

// es6
const Fn = (arg) => {...}

// 인자가 하나일 경우 괄호를 생략할 수 있습니다.
const Fn = arg => {...}

// 화살표 함수의 유일한 문장이 'return'일때 'return'과 중괄호를 생략할 수 있습니다.
const Fn = arg => console.log(arg)

// destructuring 매개변수를 이용하여 아래와 같은 방법도 응용 가능합니다.
const Fn = ({length}) => length
console.log(Fn('12345')) // 5
```

Arrows Function은 자신을 this로 바라보지 않습니다 이때 this의 범위는 함수를 둘러싸는 렉시컬 범위가 됩니다. 가급적이면 화살표 함수를 이용할 때 this를 쓰지 않는 것을 추천 드립니다.

```jsx
// Function
const obj1 = {
  age: 14,
  getAge: function () {
    return this.age;
  },
};
obj.getAge(); // 14

// Arrows Function
const obj = {
  age: 14,
  getAge: () => {
    return this.age;
  },
};
obj.getAge(); // undefined
```

<br />
 
## Class

프로토타입을 사용하던 객체 지향 방식에서 Class가 등장함에 따라 더욱 쉽게 프로그래밍이 가능해졌습니다. 하지만 Class도 내부적으론 프로토타입을 이용합니다.

```jsx
class Foo {
  constructor() {
    this.value = 100;
  }

  getValue() {
    return this.value;
  }
}

const foo = new Foo();
foo.getValue(); // 100
```

<br />
 
## Shothand

객체의 key와 value가 같다면 이를 축약하여 사용할 수 있습니다. 이를 Shothand라 부르기도 하고 Enhanced Object Literals라고 부르기도 합니다.

```jsx
const name = "Woogie";

const user = {
  name, // name: name 축약
  age: 10,
};
```

<br />
 
## Template literals

Template literals는 문자열 안에 데이터를 넣을 수 있게 합니다. 보다 편리하게 문자열을 구성할 수 있습니다.

```jsx
let name = "Woogie";
let age = 10;
// es5
let user = "user - " + name + " age - " + age; // 'user - Woogie age - 10'
// es6
let user = `user - ${name} age - ${age}`; // 'user - Woogie age - 10'
```

<br />
 
## Destructuring

구조 분해 할당이라고도 불리며 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 표현식입니다.

```jsx
let [a, b] = [1, 2, 3];
console.log(a); // 1
console.log(b); // 2

// 공백을 넣어 반환 값을 무시할 수 있습니다.
// spread를 이용해 나머지를 한번에 가져올 수 있습니다.
let [a, , b, ...arg] = [1, 2, 3, 4, 5];
console.log(a); // 1
console.log(b); // 3
console.log(arg); // [4,5]

// 객체에서도 사용 가능합니다.
let { a, b } = { a: 10, b: 20 };
console.log(a); // 10
console.log(b); // 20

// 선언 후 분해 할당
let a, b;
[a, b] = [1, 2];
console.log(a); // 1
console.log(b); // 2

// default, 기본값 분해한 값이 undefined라면 기본값을 대신 사용합니다.
let a, b;
[a = 10, b = 20] = [1];
console.log(a); // 1
console.log(b); // 20

// 두 변수의 값을 교환할 수 있습니다.
let a = 10;
let b = ((20)[(a, b)] = [b, a]);
console.log(a); // 20
console.log(b); // 10
```

<br />
 
## Rest

Rest 파라미터는 인자로 넘어온 여러개의 인자들을 하나의 배열로 묶어줍니다.

```jsx
const fn = (...rest) => {
  return rest;
};

fn(1, 2, 3, 4, 5); // [1,2,3,4,5]
```

<br />
 
## Spread

Spread는 반복 가능한 배열, 문자열, 객체를 개별 요소로 분리 시킬 수 있습니다.

```jsx
// 배열을 결합할 수 있습니다.
const a = [1, 2, 3, 4, 5];
const b = ["a", "b", ...a];
console.log(b); // ['a','b',1,2,3,4,5]

// 배열을 복사할 수 있습니다. 이때 복사한 배열은 참조가 끊깁니다.
const a = [1, 2, 3];
const b = [...a];
console.log(a === b); // false

// 문자열에도 사용 가능합니다.
const str = "string";
console.log([...str]); // ['s','t','r','i','n','g']

// 객체에서도 가능합니다.
const obj = { a: 10, b: 20 };
const obj2 = { ...obj, c: 30 };
console.log(obj2); // {a: 10, b: 20, c: 30}

// 만약 객체에 같은 key가 있다면 해당 key는 업데이트가 됩니다.
const obj = { a: 10, b: 20 };
const obj2 = { ...obj, a: 30 };
console.log(obj2); // {a: 30, b: 20}
```
