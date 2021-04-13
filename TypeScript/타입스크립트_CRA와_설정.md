# 타입스크립트 CRA

타입스크립트와 리액트를 같이 쓰려면 복잡한 초기 세팅을 하나하나 해줘야 했습니다. 하지만 요즘엔 CRA가 타입스크립트까지 자동으로 완성 시켜줍니다. 복잡한 프로젝트나 실무에서는 직접 초기 세팅을 하여 자기 입맛대로 꾸려 사용할 수도 있지만 간단한 토이 프로젝트나 사이드 프로젝트를 한다면 간편하게 CRA를 이용해도 됩니다.

타입스크립트 CRA 사용법은 기존 CRA 명령어와 비슷합니다. 다만 뒤에 `—template typescript` 라는 명령어를 추가해주기만 하면 됩니다.

```json
$ npx create-react-app 폴더명 --template typescript
```

<br />
 
# 타입스크립트 설정

타입스크립트에는 설정을 할 수 있는 파일인 `tsconfig.json` 파일이 있습니다. tsconfig 파일은 타입스크립트가 어떻게 컴파일할 건지 컴파일러 옵션을 통해 설정할 수 있도록 해주는 파일입니다.

<br />
 
# 타입스크립트 설정 속성

타입스크립트 설정 파일에는 아래와 같이 컴파일러 옵션과 여러 속성으로 이루어져 있습니다.

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
```

옵션과 속성은 너무 많고 이미 문서화가 잘 되어 있어 링크로 대체합니다.

[컴파일러 옵션 Doc](https://typescript-kr.github.io/pages/compiler-options.html)

[타입스크립트 파일 속성](https://joshua1988.github.io/ts/config/tsconfig.html#%ED%83%80%EC%9E%85%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%84%A4%EC%A0%95-%ED%8C%8C%EC%9D%BC-%EC%9D%B8%EC%8B%9D-%EA%B8%B0%EC%A4%80)
