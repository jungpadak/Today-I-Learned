# 데이터 타입


프로그래밍 언어에선 데이터에 타입이란게 존재하는데 예를 들어 숫자 1과 문자 '1'은 비슷하게 보이지만 서로 다른 타입입니다. 숫자 타입은 연산을 위해 만들지만 문자열 타입은 주로 텍스트로 출력하기 위해 만들어집니다.

자바스크립트엔 총 7가지 타입이 존재합니다.

- 원시 타입
    - string
    - number
    - boolean
    - undefined
    - null
    - symbol ( ES6에서 추가 )
- 객체 타입
    - object

## 1. String (문자열)


String 타입은 텍스트 데이터를 나타냅니다. 

```jsx
let string = 'text' // String 타입은 ''나 "" 혹은 ``로 감싸져 있습니다.
```

## 2. Number (숫자형)

Number 타입은 숫자입니다. 숫자를 이용해서 간단하거나 복잡한 연산도 가능합니다.

C나 Java의 경우엔 숫자 타입도 int, long, float, double 등 다양한 타입이 존재하지만 자바스크립트는 단 하나의 타입만 존재합니다. 

그러므로 정수도 실수도 음의 정수, 2진수 , 8진수 등 모든 숫자는 Number 타입입니다.

```jsx
let integer = 10;        // 정수
let double = 10.12;      // 실수
let negative = -20;      // 음의 정수
let binary = 0b01000001; // 2진수
let octal = 0o101;       // 8진수
let hex = 0x41;          // 16진수
```

## 3. Boolean

Boolean 타입은 논리적 참, 거짓을 나타내는 `true`와 `false` 뿐입니다. Boolean 타입은 조건문에서 자주 사용됩니다.

```jsx
var person = true;
var animal = false;
```

## 4. Undefined

Undefined 타입은 비어있는 값을 가져올때 `undefined` 값을 반환시킵니다. 변수를 만들고 값을 정의하지 않거나 존재하지 않은걸 할당 하였을때 `undefined` 가 반환됩니다.

```jsx
let test; 
console.log(test) // undefined

function testFn(){
	return
}
console.log(testFn) // undefined
```

## 5. Null

Null은 Undefined와는 다르게 의도적으로 변수에 값이 없다는 것을 명시할 때 사용됩니다.

```jsx
let test = null // null
```

## 6. Symbol

심볼은 ES6에서 새롭게 추가된 타입으로 변경 불가능한 원시 타입의 값이다. 심볼은 주로 이름의 충돌 위험이 없는 유일한 객체의 Property Key를 만들기 위해 사용한다.

```jsx
// 심볼 key는 이름의 충돌 위험이 없는 유일한 객체의 프로퍼티 키
var key = Symbol('key');
console.log(typeof key); 	// symbol

var obj = {};
obj[key] = 'value';
console.log(obj[key]);  	// value
```

## 7. 객체 타입

원시 타입을 제외한 나머지 값들( 배열, 함수, 정규표현식 등 )은 모두 객체 타입입니다.

```jsx
const testFn = () => {} // function Type
const testArr = [] // object
const testObj = {} // object
```

다른 프로그래밍 언어에는 array라는 타입이 따로 존재하지만 자바스크립트에선 object로 구분된다.

그럼 object와 array는 어떻게 구분할까?

```jsx
let testArr = []

Array.isArray(testArr) // true
```

Array.isArray() 메소드를 이용하면 배열인지 확인이 가능하다.