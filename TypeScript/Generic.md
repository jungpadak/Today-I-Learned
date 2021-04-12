# Generic

제네릭은 자바스크립트에선 사용되지 않는 용어라 많이 생소한 용어이지만 타입스크립트에선 아주 강력한 개념으로 자리 잡혀 있습니다. 제네릭을 이용하게 되면 고정 적이던 타입을 조금 더 유연하게 적용 시킬 수 있고 타입이 고정되지 않으므로 함수나 클래스의 재사용성을 높여줄 수 있습니다. 제네릭을 이해하기 위해서 기존의 고정된 타입을 가진 함수의 단점을 예를 들어 설명해보겠습니다.

```tsx
const log = (text: string) => console.log(text);

console.log(log("abc"));
console.log(log(123)); // Type error

const logNum = (text: number) => console.log(text);
```

위의 `log` 함수처럼 인자의 타입을 스트링으로 고정 시킴으로서 다른 타입은 해당 함수를 사용하지 못하게 됩니다. 이를 해결하기 위해 `logNum` 함수라는 비슷한 함수를 만들어 넘버 타입을 넣어도 같은 기능을 하게 만들어 줬습니다.

<br />
 
위의 코드는 당연히 올바르지 않은 코드이고 타입 별로 같은 함수를 계속해서 만든다고 생각을 한다면 끔찍한 코드가 되지 않을까 싶습니다. 이를 간단하게 해결하기 위해 유니온 타입을 사용할 수 있습니다.

```tsx
const log = (text: string | number) => text;
```

이렇게 다양한 타입을 한번에 지정해 조금 더 유연하게 작성할 순 있지만 이 또한 문제가 생깁니다.

```tsx
const log = (text: string | number) => text;

const logStr = log("abc");
logStr.split(""); // Error
```

`log` 함수에 타입을 지정하지 않아 해당 함수는 타입 추론으로 인해 `string | number` 라는 유니온 타입을 기본적으로 가지고 있게 됩니다. 이런 유니온 타입으로 인해 변수로 선언한 `logStr`는 문자열이 아니므로 split 메소드를 사용할 수 없게 되는 문제가 생깁니다.

<br />
 
고정된 타입으로 인한 문제들 때문에 자주 사용되는 개념이 제네릭입니다. 제네릭을 이용하면 인자로 들어온 타입을 함수의 타입으로 지정 시켜 주어 위의 문제들이 해결됩니다. 제네릭은 `<>` 괄호 안에 원하는 문자를 적어 사용합니다.

```tsx
const log = <T>(text: T): T => text;

const logStr = log("abc");
const logNum = log(100);
logStr.split("");
logNum += 100;
```

위의 코드는 제네릭으로 인해 인자로 들어간 타입이 곧 함수의 타입이 되므로 각각 변수의 타입에 맞는 기능들을 사용할 수 있게 되었습니다.

<br />
 
제네릭을 활용하면 여러가지의 상황을 만들 수 있습니다. 아래 예제는 인터페이스로 틀을 만든 객체를 제네릭을 이용하여 재사용성을 높여주는 예제입니다.

```tsx
// Good
interface Text<T> {
  text: T;
  createAt: number;
}

const todo: Text<string> = { text: "Todo", createAt: 20210412 };
const todo2: Text<number> = { text: 100, createAt: 20210412 };

// Bad
interface Text {
  text: string;
  createAt: number;
}

interface TextNum {
  text: number;
  createAt: number;
}

const todo: Text = { text: "Todo", createAt: 20210412 };
const todo2: TextNum = { text: 100, createAt: 20210412 };
```

위 코드도 마찬가지로 인터페이스가 중복 되는걸 제네릭으로 해결해주었습니다.

<br />
 
 # 정리
 
제네릭을 잘 사용하면 코드의 재사용성을 높일 수 있고 코드를 보기 간결해진다는 장점이 있습니다. 이러한 장점때문에 타입스크립트로 만들어진 라이브러리를 보면 제네릭을 많이 사용한 것을 볼 수 있습니다.
