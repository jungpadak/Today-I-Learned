# Pre Week 4 Weather API

![](./image/weather_api.gif)

코드스테이츠 마지막 4주차의 과제 Weather API입니다. fetch를 이용해서 api를 호출하고 다루는 작업을하는 과제였습니다. 과제 조건은 아래와 같습니다.

- [OpenWeather API](https://openweathermap.org/) 를 통해 날씨 정보를 가져올 수 있어야 합니다.
- 가져온 데이터를 DOM을 이용해 웹 앱에 표시할 수 있어야 합니다.
  - 다음 데이터는 필수입니다.
    - 현재 온도
    - 현재 날씨
    - 선택한 도시
- 웹 앱은 사용자 입력을 받아 도시를 선택할 수 있어야 합니다.

테스트 케이스는 없습니다. 다음 가이드를 따라가되 자유롭게 디자인하고 구현해 주세요.

간단하게 설명해서 fetch를 사용해서 API를 호출 후 받아온 데이터를 화면에 출력하고 디자인을 자유롭게하는 과제입니다. 저에게는 크게 어렵지않은 과제여서 무엇을 더 추가할까 생각하다가 간단하게 날씨에 따라 배경화면이 바뀌는 기능과 시계를 추가적으로 만들었습니다.

<br />
 
## fetch를 이용해 API 호출

```jsx
function getData(name) {
  const API_KEY = "522f563b88b45d9f1003bda006f894b4";
  let API_URL_OpenWeatherMap = `http://api.openweathermap.org/data/2.5/weather?q=${name}&appid=${API_KEY}`;

  fetch(API_URL_OpenWeatherMap)
    .then(function (res) {
      if (!res.ok) {
        alert("찾는 도시가 없습니다.");
        document.querySelector(".search_input").value = "";
      }
      return res.json();
    })
    .then(function (data) {
      renderWeatherData(data);
    });
}
```

자바스크립트를 배우면서 fetch를 써본건 이번이 첨이지만 다른 것들과 형식이 크게 다르지 않아서 사용하는데 어렵진 않았습니다.

API key와 API를 따로 `API_KEY` `API_URL_OpenWeatherMap` 라는 변수에 할당해주었고 `fetch(API_URL_OpenWeatherMap)`를 이용해서 API를 호출했습니다.

![](./image/weather_api.gif)

```jsx
.then(function (res) {
      if (!res.ok) {
        alert("찾는 도시가 없습니다.");
        document.querySelector(".search_input").value = "";
      }
      return res.json();
    })
```

위 로직은 도시를 검색해서 데이터를 호출할때 존재하지 않는 도시를 넘겼다면 `res.ok`가 false가 되므로 false일때 경고 창이 뜨게 만드는 로직입니다. 경고창이 뜨고 input의 value도 지워주게끔 만들었어요

```jsx
.then(function (data) {
      renderWeatherData(data);
 });
```

다음은 코드 그대로 API에서 받아온 데이터를 처리하기 위해 함수에 전달시켜 호출시키는 로직입니다. 호출 된 함수는 화면에 데이터를 뿌려주기 위한 로직을 담아뒀어요!

<br />
 
## DOM을 이용해 데이터를 화면에 출력

![](./image/weather_api.gif)

```jsx
function renderWeatherData(data) {
  const body = document.body;
  const cityName = document.querySelector(".city_name");
  const temp = document.querySelector(".temp");
  const image = ["./image/cloud.jpg", "./image/sunny_day.jpeg", "./image/rain.jpg", "./image/snow.jpg"];
  const c = (data.main.temp - 273.15).toFixed(1);
  const f = (c * 1.8 + 32).toFixed(1);

  if (data.weather[0].main === "Clouds") body.style.backgroundImage = `url(${image[0]})`;
  if (data.weather[0].main === "Clear") body.style.backgroundImage = `url(${image[1]})`;
  if (data.weather[0].main === "Rain") body.style.backgroundImage = `url(${image[2]})`;
  if (data.weather[0].main === "Snow") body.style.backgroundImage = `url(${image[3]})`;

  cityName.textContent = data.name;
  temp.textContent = `${f}F / ${c}C`;
}
```

전체적인 로직은 위와 같습니다. `renderWeatherData(data)` 전달 인자로 데이터를 가져와 도시 이름, 날씨, 온도를 화면에 뿌려주려고 합니다. 도시 이름과 날씨는 문자 그대로 사용이 가능하지만 온도는 Kelvin이라는 단위이기 때문에 섭씨로 바꿔서 사용해야 했습니다.

```jsx
const c = (data.main.temp - 273.15).toFixed(1);
const f = (c * 1.8 + 32).toFixed(1);

temp.textContent = `${f}F / ${c}C`;
```

저는 섭씨와 화씨를 같이 쓰려고 둘 다 만들었어요 섭씨는 `Kelvin 온도 - 273.15`를 하면 나오고 화씨 온도는 `섭씨 온도 * 1.8 + 32`를 하면 구할 수 있어요 온도가 소수점까지 나오기 때문에 `toFixed`를 이용해 소숫점 첫자리까지만 나오게 만들었습니다. 그리고선 준비해둔 태그에 뿌려줬어요

![](./image/weather_api_2.gif)

```jsx
const image = ["./image/cloud.jpg", "./image/sunny_day.jpeg", "./image/rain.jpg", "./image/snow.jpg"];

if (data.weather[0].main === "Clouds") body.style.backgroundImage = `url(${image[0]})`;
if (data.weather[0].main === "Clear") body.style.backgroundImage = `url(${image[1]})`;
if (data.weather[0].main === "Rain") body.style.backgroundImage = `url(${image[2]})`;
if (data.weather[0].main === "Snow") body.style.backgroundImage = `url(${image[3]})`;
```

위의 로직은 받아 온 데이터의 날씨에 따라 변경 될 배경 화면을 배열에 담아주고 조건문으로 날씨에 맞는 이미지를 뿌려주는 로직입니다. 이 로직은 도시가 변경 될 때 이미지가 부드럽게 바뀌게 하기 위해 CSS에 `transition`을 줬습니다.

<br />
 
## 사용자가 입력한 도시 데이터를 가져오기

```jsx
function search() {
  const searchInput = document.querySelector(".search_input");

  searchInput.addEventListener("change", function (e) {
    e.preventDefault();
    getData(searchInput.value);
    searchInput.value = "";
  });
}
```

사용자가 input에 도시 이름을 적고 엔터를 치면 도시가 변경되는 로직입니다. 따로 설명 드릴 부분이 없네요!

<br />
 
## new Date()를 이용해 시계 만들기

```jsx
function timeStamp() {
  const time = document.querySelector(".time");

  time.textContent = `${new Date().getHours()}:${m()}`;

  setInterval(function () {
    console.log("1");
    time.textContent = `${new Date().getHours()}:${m()}`;
  }, 10000);

  function m() {
    if (new Date().getMinutes() < 10) {
      return `0${new Date().getMinutes()}`;
    } else {
      return new Date().getMinutes();
    }
  }
}
```

시간이 많이 남아서 시계를 넣어보자는 페어분의 아이디어에 `new Date()`를 이용한 시계를 만들어 보았습니다. 처음엔 `setInterval`로 간단하게 만들면 되겠다 싶었는데 예상치 못한 상황이 발생하더라고요 분이 1~9분일때 01분 02분이라 뜨지 않고 1분 2분 이런식으로 떠서 시계 모양이 일그러지는 문제를 확인했어요 그래서 아래 `m` 함수를 만들어 10 아래의 분들은 0을 넣어주게끔 처리했습니다.

<br />
 
## 회고

이번 과제는 따로 생각하지 않고 과제날 즉흥적으로 생각하고 만든거라 무언가 더 대단한 기능은 없습니다. 그나마 디자인이 깔끔하게 잘 나와서 맘에 드네요! 이제 앞으로 이머시브 코스에 들어가게 될텐데 이머시브의 과제는 어떨지 매우 기대가 됩니다.
