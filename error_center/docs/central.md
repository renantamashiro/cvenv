# Central de Erros

*API para cadastro e controle de erros*	

A Central de Erros é uma API que permite aos seus usuários consultarem os logs registrados pela sua equipe. Possui ordenação de logs por ocorrências, levels e segregação por categorias. Somente usuários autenticados pelo administrador poderão acessar os logs registrados, garantindo total segurança das informações registradas pela equipe.

**Tópicos**:

[TOC] 

## Requisitos



### Funcionais

|#|Descrição|Categoria|
|--|--|--|
|rf1|A API deve possuir um usuário administrador para controlar os usuários da API|Essencial|
|rf2|Deve ser possível cadastrar n usuários e, cada um, deve possuir um token de autenticação|Essencial|
|rf3|Deve ser possível cadastrar x logs por usuários. Cada log conterá sua categoria, level, título, descrição, origem, data de ocorrência e quantidade de ocorrências (eventos)|Essencial|
|rf4|Os logs poderão ser arquivados ou excluídos e tal procedimento deve ser feito de modo otimizado (selecionar vários para fazer esse procedimento)|Essencial|
|rf5|Deve ser possível ordenar por level e frequência, assim como realizar buscas customizadas|Essencial|



### Não funcionais

|#|Descrição|Categoria|
|--|--|--|
|rnf1|O banco de dados deve ser relacional (PostgreSql)|Essencial|
|rnf2|Todos os modelos criados deverão ser testados (aplicar TDD)|Essencial|
|rnf3|As dependências do sistema devem ser controlados de modo automatizado|Essencial|
|rnf4|Somente usuários autenticados poderão consultar e editar os dados da API (utilizar JWT)|Essencial|
|rnf5|A api deve ser documentada|Essencial|



## Wireframes e diagramas

|Login|Página principal|
|---|----|
|![image-20200703235509690](/home/renan/.config/Typora/typora-user-images/image-20200703235509690.png)|![image-20200703235550608](/home/renan/.config/Typora/typora-user-images/image-20200704001320028.png)|

|User cases|
|:--------------:|
|<img src="/home/renan/.config/Typora/typora-user-images/image-20200704001453916.png" alt="image-20200704001453916" style="zoom:50%;" />|

|Relação entre as entidades|
|:----:|
|<img src="/home/renan/.config/Typora/typora-user-images/image-20200704214402534.png" alt="image-20200704214402534" style="zoom:67%;" />|



## Brief - API

|Página|URL|Requisitos|
|----|----|----|
|Página inicial de logs|`/logs/`|Lista todos os logs cadastrados pelos usuários autenticados|
|Exibição por categoria|`/logs/<group>`|Exibir logs por grupo|
|Ordenação|`/logs/<sort-type>`|Ordenar os logs por frequência e level|
|Buscar logs|`/logs/<filter?q=param>`| Buscar logs por determinada característica|
|Inserir log|`/logs/insert`|Inserir log (pegar parâmetros no corpo da requisição POST)|
|Deletar log|`/logs/delete/<pk>`| Deletar determinado log pelo pk|
|Arquivar log| `/logs/archive/<pk>`     | Arquiva os logs                                              |
|Consultar detalhes do log|`/logs/<pk>`|Consulta os detalhes de cada log, como: título, origem, data, descrição etc.|
|Página usuário|`/logs/user`|Retorna os dados do usuário na sessão|
|Encerrar sessão|`/logs/user/logout`|Encerra a sessão do usuário|




