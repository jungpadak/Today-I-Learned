# BEM 방법론

개발을 하다보니 가장 어렵게 느껴지는게 네이밍이 아닐까싶습니다. 좋은 네이밍? 의미 전달이 잘 되는 네이밍? 저한테는 조금 어렵더라고요 이 네이밍은 HTML에서도 저를 힘들게하는데요 class의 이름을 어떻게 지어주어야 좋을지 고민이 됩니다. 좋은 네이밍은 코드의 가독성을 높혀주고 그에 따라 일의 효율성 또한 올라갑니다. 클래스명을 잘 짓고자 CSS에는 여러가지 방법론들이 있습니다. 이 방법론 중에 BEM 방법론을 알아보려합니다.

<br />
 
## Block / Element / Modifier

Block / Element / Modifier를 줄여서 BEM이라 부르는데 각각의 의미를 간단하게 적자면 Block은 영역을 Element는 영역에 포함된 조각 Modifier는 영역 또는 조각의 속성을 의미합니다. BEM 방법론은 이러한것들을 조합하여 클래스명을 만들어요

<br />
 
## Block

Block은 Element를 담고 있는 컨테이너, 큰 덩어리라고 생각하면 됩니다. 헤더 메인 컨텐츠 풋터 이러한 단위들을 생각하면 쉽게 이해가 되죠?

<br />
 
## Element

Element는 Block에 포함되어 있는 조각을 의미합니다. 예를 들자면 header 안에 logo와 nav가 있다면 이 logo와 nav가 Element가 되는거죠 이제 Block과 Element를 이용해서 클래스명으로 작성해보면 `header__logo` 와 같은 형태가 됩니다. Block과 Element를 `__` 언더바 두개로 연결해 작성합니다.

```css
.header__logo {
}
.header__nav {
}
.header__serchbar {
}
```

두개의 언더바로 구분하여 시각적으로 쉽고 빠르게 코드를 찾게 도와줍니다 Element를 작성할땐 명확하고 정확하게 작성해야 합니다. div 태그라 해서 `.header__div` 이런식으로 작성하는 일은 없어야겠죠?

<br />
 
## Modifiers

Modifiers는 Block 또는 Element의 속성을 의미하는데요 색상이나 사이즈, 상태를 작성합니다. 작성법은 `--` 하이픈을 두개로 연결해 작성하는데요 붙여서 써보자면 `header__logo--big` 과 같은 형태로 작성합니다.

```css
.header__logo--big {
}
.header--small {
}
.header__serchbar--on {
}
.header__serchbar--off {
}
```

<br />
 
BEM 방법론대로 작성하면 클래스명이 길어질순 있습니다. 하지만 재사용에 용이하고 직관적이라는 장점이 있습니다.
