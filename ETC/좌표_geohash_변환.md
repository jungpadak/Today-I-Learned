# 좌표 geohash로 변환하기

geohash 코드를 쓸 일이 생겨 관련 라이브러리가 있나 찾던 중 간단하게 변환할 수 있는 방법을 찾았다.

[Latlon-geohash Link](https://www.npmjs.com/package/latlon-geohash)

# 웹에서 불러오기

```js
import Geohash from "https://cdn.jsdelivr.net/npm/latlon-geohash@2.0.0";
```

원하는 파일에 Geohash를 불러오고 HTML에서 script를 불러올때 아래와 같이 불러야 한다 **꼭!!**

```html
<script type="module" src="..." />
```

좌표를 geohash로 바꿔주는 인코딩과 그 반대인 디코딩만 간단하게 적어둡니다.

# encode

lat과 lon은 좌표를 적으면 되고 precision은 geohash의 자릿수를 적으면 된다. 자릿수가 작을 수록 큰 범위를 나타낸다.

```js
// Geohash.encode(lat, lon, [precision])
const geohash = Geohash.encode(37.49159755, 127.0083737, 5);
console.log(geohash); // wydm7
```

# deocde

반대로 geohash 값을 이용하여 좌표를 얻을 수 있다.

```js
// Geohash.decode(geohash)
const latlon = Geohash.decode("u120fw");
console.log(latlon); // {lat: 37.507, lon: 127.068}
```
