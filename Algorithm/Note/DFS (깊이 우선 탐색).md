# DFS (깊이 우선 탐색)

- #### 인접행렬

  - 2차원 배열을 활용하여 그래프를 표현하는 방식

![image-20230214212841926](C:\Users\jyr49\AppData\Roaming\Typora\typora-user-images\image-20230214212841926.png)

```markdown
- 장점 : 두 노드의 간선의 존재 여부를 바로 알 수 있음
- 단점 : 모든 관계를 기록함으로 노드의 개수가 많을 수록 불필요한 메모리 낭비가 일어남
ex) 그래프에 간선이 많이 존재하는 밀집 그래프
```

- #### 인접 리스트

  - 연결 리스트를 활용하여 표현하는 방식

![image-20230214212919882](C:\Users\jyr49\AppData\Roaming\Typora\typora-user-images\image-20230214212919882.png)

![image-20230214212937350](C:\Users\jyr49\AppData\Roaming\Typora\typora-user-images\image-20230214212937350.png)

```markdown
- 장점 : 연결된 것들만 기록함 / 어떤 노드의 인접한 노드들을 바로 알 수 있음
- 단점 : 두 노드가 연결되어 있는지 확인이 인접 행렬보다 느림
ex) 간선이 적은 희소 그래프
```

