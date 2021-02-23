# GIT 명령어 모음

## Git 저장소 생성

### git init

이 명령은 `.git`이라는 하위 디렉토리를 만듭니다. 저장소에 필요한 파일들이 들어있습니다.

```scss
$ git init
```

<br />
 
## Git 추가, 확정, 업로드

### git add

commit에 변경 사항을 포함 시킵니다.

```scss
$ git add <파일명>
```

### git commit

add에서 전달된 commit을 확정 시킵니다.

```scss
$ git commit -m "메세지"
```

### git push

commit까지 완료된 변경 사항들을 원격 서버에 업로드합니다.

```scss
$ git push <remote 이름> <branch>
```

<br />
 
## Git 상태 확인

### git status

현재 파일들의 상태를 확인합니다.

```scss
$ git status
```

### git log

현재 위치한 브랜치의 커밋을 확인 할 수 있습니다.

```scss
$ git log
```

<br />
 
## Git 복제

### git clone

원격 저장소의 내용을 그대로 복사해 옵니다.

```scss
$ git clone <URL>
```

<br />
 
## Git 갱신, 병합

### git pull

원격 저장소의 내용을 로컬 저장소로 가져옵니다 이 과정에서 fetch와 merge가 됩니다.

```scss
$ git pull
```

### git merge

현재 브런치와 다른 브랜치의 변경 내용을 병합합니다.

```scss
$ git merge <다른 브랜치 이름>
```

### git diff

서로 다른 브랜치의 바뀐 내용을 비교 할 수 있습니다.

```scss
$ git diff <브랜치> <다른 브랜치>
```

<br />
 
## Git 브랜치 생성, 이동, 삭제

### git branch

브랜치 목록을 불러옵니다.

```scss
$ git branch
```

### git brancg <이름>

새로운 브랜치를 생성합니다.

```scss
$ git branch <이름>
```

### git checkout <이름>

다른 브랜치로 이동합니다.

```scss
$ git checkout <이름>
```

### git push <remote 이름> <branch 이름>

생성한 브랜치를 원격 저장소로 전송합니다.

```scss
$ git push <remote 이름> <branch 이름>
```

<br />
 
## Git 되돌리기

### git reset

특정 커밋으로 돌아갑니다. 대신 커밋들이 지워집니다. 보통 혼자서 사용하는 브랜치일 때 사용합니다.

```scss
$ git reset --hard <커밋 주소> // hard는 현재 커밋과 돌아간 커밋 사이의 모든 커밋들이 사라집니다.

$ git reset --mixed <커밋 주소> // mixed는 삭제되지 않고 변경 사항들이 add하기 전 상태로 돌아갑니다.

$ git reset --soft <커밋 주소> // soft는 mixed와 같지만 add가 된 상태로 돌아갑니다.
```

### git revert

revert는 특정 커밋으로 돌아가지만 커밋들이 지워지지 않고 돌아간 커밋을 추가합니다. reset —soft와 mixed와 비슷한 결과를 가져오지만 커밋은 남아있는거죠

```scss
git revert <커밋 주소>
```
