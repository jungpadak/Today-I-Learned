# 변수 (Variable)

변수는 데이터를 담기위한 메모리 공간인데요 조금 쉽게 이야기하자면 데이터를 보관하는 보관함 같은 역할을 합니다.

보관함(메모리)이 있고 이 보관함에 이름을 정해줍니다. ( 선언 )

```jsx
let age; // 변수에 이름을 지정해주는것이 선언!
```

보관함의 이름을 `age` 로 선언해 주었고 이 곳에 데이터를 보관해 봅시다. ( 할당 )

```jsx
age = 28; // 변수에 데이터를 넣는것이 할당!
```

보관함의 이름으로 보관함 안에 있는 데이터를 가져와서 사용 가능합니다.

```jsx
console.log(age); // 28
```

만약 할당을 하지 않는다면 변수의 데이터는 어떻게 될까요?

```jsx
let age;

console.log(age); // undefined ( 정의되지 않은 값 )
```

당연히 `age`라는 보관함에 데이터가 담겨있지 않으니 찾을 수가 없습니다. 고로 undefined를 반환합니다.

선언과 할당은 한번에 해줄 수도 있습니다.

```jsx
let age = 28;

console.log(age); // 28
```

변수 안에는 어떤 데이터든지 넣을 수 있고 원하는 만큼 데이터를 변경할 수도 있습니다.

```jsx
// case 1 //
let age = 28;
age = 5;
console.log(age); // 5

// case 2 //
let num = 10;
num = num + 5;
console.log(num); // 15
num = num + 15;
console.log(num); // 30
```

데이터가 변경되면 이전 데이터는 변수에서 제거가 됩니다.

이렇게 할당한 변수를 이용해서 새로운 변수를 만들 수도 있습니다.

```jsx
// case 1 //
let name = "Woogie";
let myNameIs = "My Name Is";
let greeting = myNameIs + name;
console.log(greeting); // 'My Name Is Woogie'

// case 2 //
let num1 = 10;
let num2 = 3;
let result = num1 + num2;
console.log(result); // 13
let result2 = result + num1;
console.log(result2); // 23
```

> ⚠️ 변수를 두 번 선언하면 에러가 발생합니다.
>
> ```js
> let age = 28;
> let age = 27; // SyntaxError: 'message' has already been declared
> ```
>
> 따라서 변수는 딱 한번만 선언하자

# 변수명 규칙

변수명을 짓는데 규칙이 있습니다.

1. 변수명은 오로지 문자, 숫자만 들어갈 수 있습니다.
2. 예외로 `$` 와 `_` 는 사용 가능합니다.
3. 변수명의 첫 글자로 숫자가 들어가면 안됩니다.

```jsx
// 잘못된 예시 //
let %^&; // 문자, 숫자 외의 문자가 들어갈순 없습니다.
let 123test; // 첫 글자로 숫자를 사용하면 안됩니다.
let one-two; // '-'은 사용이 불가능합니다.

// 좋은 예시 //
let $test;
let _test;
let test123;
let one_two;
let frontEndDev;
```

변수명을 지을땐 camelCase라는 표기법도 있습니다. 여러 단어를 조합할때 첫 단어를 제외한 각 단어의 첫 글자를 대물자로 작성합니다.

```jsx
let camelCase;
let userAge;
let myNameIs;
```

글자가 낙타 등같다고 해서 카멜케이스라고 불리웁니다.

변수명은 대소문자도 구별합니다

```jsx
// 두 변수는 전혀 다른 변수입니다.
let home;
let Home;
```

자바스크립트엔 [예약어](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)라는 단어가 있습니다. 예약어로 지정된 단어는 변수명으로 사용할 수 없습니다.

```jsx
let function; // function이라는 예약어가 있으므로 에러
let for; // for이라는 예약어가 있으므로 에러
```

# Const

변수를 선언하기 위해선 `let` 말고도 `const` 라는 것도 있습니다. `const` 는 `let` 과 다르게 할당한 데이터를 변경할 수 없습니다.

```jsx
const name = "Woogie";

name = "Minsoo"; // Uncaught TypeError: Assignment to constant variable.
```

`var`라는 변수도 있는데 이는 오래된 변수 키워드입니다. 여러가지 문제점이 있고 개선된 `let` 과 `const` 가 등장하면서 사용하지 않는 키워드가 됐습니다.
