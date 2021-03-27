# Props

props는 컴포넌트의 속성을 설정할 때 사용됩니다. props 값은 해당 컴포넌트를 불러와 사용하는 부모 컴포넌트에서 설정할 수 있습니다.

props는 상위 컴포넌트에서 하위 컴포넌트로 전달하는 개념이며, 하위 컴포넌트에서 상위 컴포넌트에 값을 전달할 수 없습니다.

<br /> 
 
## 컴포넌트를 사용할 때 props 값 지정하기

App 컴포넌트에서 User 컴포넌트의 props 값을 지정해 봅시다.

```javascript
const App = () => (
  <div>
    <User name="Woogie" />
  </div>
);

const User = (props) => <h1>{props.name}</h1>;
```

이런식으로 부모 컴포넌트에서 자식 컴포넌트 태그에 속성과 값을 지정해주면 자식 컴포넌트는 그 속성을 받아와 값을 추출할 수 있습니다.

<br /> 
 
## 태그 사이의 내용을 보여 주는 children

children은 컴포넌트 태그 사이에 있는 내용을 보여주는 props입니다.

```javascript
const App = () => {
  <div>
    <User>React</User>
  </div>;
};

const User = (props) => {
  <h1>{props.children}</h1>;
};
```

User 태그 사이에 있는 내용인 React를 props로 가져와 h1 태그 사이에 넣었습니다.

<br /> 
 
## 비구조화 할당 (구조 분해 할당)

비구조화 할당은 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 JavaScript 표현식입니다. 앞에선 props.name이나 props.children 같이 앞에 props를 붙여 사용하고 있었는데 이를 비구조화 할당으로 props 내부의 값을 추출하여 사용해 봅시다.

```javascript
const User = {children} => {
  <h1>{children}</h1>
}
```

이런식으로 함수의 파라미터 부분에서 사용이 가능하고 만약 age라는 props가 추가로 있다면 ({ children, age }) 이와 같이 분해하여 사용하시면 됩니다.

<br /> 
 
## propTypes를 통한 props 검증

컴포넌트의 필수 props을 지정하거나 props의 type을 지정할 때는 propTypes를 이용해야합니다. propTypes를 이용하려면 import를 사용하여 불러와야 합니다.

```javascript
import PropTypes from 'prop-types';

const User = {children} => {
  <h1>{children}</h1>
}

User.propTypes = {
	children: PropTypes.string
}
```

이렇게 설정해 주면 children 값은 무조건 string 형태로 전달이 되어야하고 다른 타입으로 전달 받게 된다면 콘솔에 경고 메시지를 출력하여 잘못되었다는것을 알려줍니다.

<br /> 
 
## isRequired를 사용하여 필수 propTypes 설정

isRequired를 붙이면 설정한 props의 타입이 다르거나 부모 컴포넌트에서 설정을 안해 줬다면 경고 메세지를 띄워 줍니다.

```javascript
import PropTypes from 'prop-types';

const User = {name} => {
  <h1>{name}</h1>
}

const App = () => {
  <div>
    <User /> // name을 지정해주지 않았으므로 콘솔에 경고 메시지가 출력됨.
    <User name="리액트" /> // 아무런 경고 없음
  </div>
}

User.propTypes = {
	children: PropTypes.string.isRequired
}
```

propTypes는 큰 규모의 프로젝트를 진행하고 다른 개발자들과 협업을 한다면 propTypes으로 해당 컴포넌트의 어떤 props가 필요한지 쉽게 알게되고 초기에 잘못을 잡을 수 있으므로 개발 능률을 좋게 하기위해 사용합니다.

<br /> 
 
## 클래스형 컴포넌트에서의 props 사용

클래스형 컴포넌트에서 props를 사용할 때에는 render 함수에서 this.props를 조회하면 됩니다.

```javascript
class User extends Component {
  render() {
    const { name } = this.props;
    return <div>{name}</div>;
  }
}
```

여기에 propTypes도 넣어보겠습니다.

```javascript
class User extends Component {
  static propTypes = {
    name: PropTypes.string.isRequired,
  };

  render() {
    const { name } = this.props;
    return <div>{name}</div>;
  }
}
```
