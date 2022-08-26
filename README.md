<h1 align="center">
    desafio web scraping-selenium
</h1>

<p>
Implementar um programa que utilize web scraping para percorrer todas as páginas do site: http://quotes.toscrape.com/ e coletar todas as citações exibidas.
As informações devem ser compiladas em um arquivo .json
</p>
## Regras:
- Para cada citação, os seguintes dados devem ser coletados: 
    - citação (*string*),
    - autor (*dictionary*) com seu nome (*string*) e url da sua bio (*string*),
    - tags (*list*).

 <br>
 
 - Criar um fork do repositório
 - Abrir um pull request ao finalizar o desafio

## Saída:
As informaçãos devem ser gravadas num arquivo `.json`, gerado a partir da execução do programa, seguindo a estrutura do dicionário: 
``` python
{
    "quote": quote,
    "author": {
         "name":author,
         "url":url
     },
    "tags":[tags]
}

```

### exemplo: 

![image](https://user-images.githubusercontent.com/92794401/185461270-73e35972-3d60-4b9c-85a1-6b50c944db70.png)

``` python
{
    "quote":"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
    "author":{
        "name":"Albert Einstein",
        "url":"http://quotes.toscrape.com/author/Albert-Einstein"
    },
    "tags":[
        "change",
        "deep-thoughts",
        "thinking",
        "world"
    ]
}
```


## Tools
Devem ser utilizadas as ferramentas:
- [Python](https://docs.python.org/3/)
- [Selenium Framework](https://www.selenium.dev/documentation/)
   
   

## Dúvidas / sugestão
Caso haja alguma dúvida ou sugestão sobre o teste, pode criar uma issue neste projeto.

<br> <br>

> Esse teste é público. Candidatos para vagas na FIX-SI devem responder este teste como parte do processo seletivo.
