# DOM이란?

DOM은 Document Object Model의 약어입니다. 객체로 문서 구조를 표현하는 방법으로 HTML이나 XML로 작성됩니다.

브라우저는 DOM을 활용하여 객체에 JS나 CSS를 적용시키고 특정 노드를 찾아 수정하거나 제거하는 등 원하는 곳에 삽입도 가능합니다.

하지만 규모가 큰 웹 어플리케이션(트위터, 페이스북) 에서는 스크롤을 내리다 보면 정말 수 많은 데이터가 로딩이 되고 각 데이터를 표현하는 요소도 많아지게 됩니다.

이와 같은 요소의 갯수가 몇백 몇천개 단위로 많아진 상태에서 DOM에 접근하며 변화를 주다보면 성능상 이슈가 발생하게 됩니다. 이를 잘 이해하기 위해 브라우저가 어떻게 작동하는지 알아봅시다.

<br />
 
# 브라우저의 Workflow

![image.png](https://images.velog.io/post-images/woogie94/ad933710-3137-11ea-8fbe-6977104b9b0c/image.png)

### **DOM Tree 생성**

브라우저가 HTML을 전달받으면 브라우저의 렌더 엔진이 이를 파싱하고 DOM 노드로 이뤄진 트리를 만듭니다. 각 노드는 각 HTML 엘리먼트들과 연관이 되어있어요. 즉, 브라우저가 HTML을 이해하고 사용 가능하게 구조를 변환하는 과정입니다.

### **Render Tree 생성**

그리고, 외부 CSS파일과 각 엘리먼트의 inline 스타일을 파싱하고 CSSDOM Tree를 빌드합니다. 그리고 DOM Tree와 CSSDOM Tree를 결합하여 Render Tree를 형성하는 과정입니다.

### **Layout**

Render Tree가 다 만들어진 후 Layout 과정을 거치게됩니다. 각 노드들은 스크린의 좌표가 주어지게 되고, 어느곳에 나타나야 하는지 각 위치에 배치가 되는 과정입니다.

### **Painting**

Painting 작업은 렌더링 된 요소들에 색을 입히는 과정입니다. 트리의 각 노드들을 거쳐가며 paint() 메소드를 호출해요. Painting 작업이 끝나면 스크린에 정보들이 나타나게 됩니다.

<br />
 
# DOM의 문제점

DOM을 조작하여 변화가 생긴다면 DOM은 렌더트리를 재생성하고 레이아웃을 만들고 페인팅 하는 과정을 다시 반복하게 됩니다. 예를 들어 100개의 노드를 하나 하나 수정하면, 100번의 레이아웃 과정과 100번의 리렌더링이 발생하게 됩니다. 큰 웹앱 같은 경우에 많은 양의 데이터가 불필요하게 리렌더링이 된다면 성능이 떨어지고 웹이 느려지게 됩니다. 이 같은 경우를 방지하고자 Virtual DOM을 사용합니다.

<br />
 
# Virtual DOM이란?

Virtual DOM이란 실제 DOM에 접근하며 조작하는 대신 이를 추상화 시킨 가벼운 사본 같은 느낌의 자바스크립트 객체를 만들어 사용합니다. DOM에 변화가 일어난다면 Virtual DOM에 업데이트가 되고 이전 Virtual DOM과 비교하여 변화된 부분만 DOM에게 전달하여 적용시킵니다. 위에서 보여준 브라우저의 Workflow를 무시하고 변화가 이뤄진 부분만 렌더링 시킴으로서 성능이 향상됩니다.
