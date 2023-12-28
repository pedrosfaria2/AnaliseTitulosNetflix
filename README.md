# 🎥 Analisando filmes da Netflix no IMDB 🎥

## Motivação: 
Você já ouviu falar do IMDb? O IMDb, também conhecido como Internet Movie Database, é uma base de dados online repleta de informações sobre filmes, programas de televisão, vídeos caseiros, jogos de vídeo e conteúdo de streaming online. Ele oferece detalhes como o ano de lançamento, gênero, elenco, equipe de produção, sinopses e até avaliações dos usuários. Além disso, o IMDb possui um sistema de classificação onde os usuários podem avaliar filmes e séries numa escala de 1 a 10.

Você costuma usar o IMDb quando está escolhendo o que assistir? Se sim, até que ponto as avaliações e classificações influenciam sua decisão? Você costuma levar em consideração a quantidade de avaliações ou a nota dada pelos usuários ao escolher o que assistir?

E quanto aos formatos de conteúdo, você assiste mais a filmes ou séries? E o conteúdo da Netflix nessas plataformas, você também costuma verificar no IMDb antes de escolher ou prefere avaliar depois de assistir para compartilhar sua opinião com outros espectadores?

Estas são algumas das questões que gostaríamos de explorar neste estudo.

## Sobre o projeto:
Este projeto se propõe a explorar um conjunto de dados do [Kaggle](https://www.kaggle.com/), que pode ser encontrado [aqui](https://www.kaggle.com/datasets/thedevastator/netflix-imdb-scores), que abrange mais de 5.000 títulos da Netflix no IMDb. As informações disponíveis incluem título, tipo (filme ou série), descrição, ano de lançamento, classificação etária, duração, ID do IMDb, avaliação do IMDb e número de votos no IMDb.

Nosso objetivo é investigar a popularidade desses títulos com base nas informações disponíveis. Pretendemos responder às seguintes perguntas:

- Como podemos medir a popularidade de um título com base nas informações disponíveis?
- Quais são os títulos mais populares?
- Filmes ou séries são mais populares?
- O tipo de conteúdo influencia a popularidade?
Nossa hipótese inicial é que o tipo de conteúdo tem impacto na popularidade, sendo as séries geralmente mais populares do que os filmes. Esta hipótese será testada ao longo do projeto.

Neste projeto, realizamos uma série de etapas, incluindo a importação de arquivos, a exploração do conjunto de dados, a correção de valores ausentes relevantes para nossa análise e a exclusão de colunas que não eram pertinentes ao nosso estudo. Além disso, desenvolvemos uma métrica para classificar a popularidade dos títulos, que envolveu a formulação da métrica e a realização de testes estatísticos para embasar nossas conclusões.

A popularidade foi determinada com base em uma ponderação das informações disponíveis, que incluem a avaliação média dos usuários e a quantidade de votos que resultaram nessa avaliação. Assim, demos maior peso à quantidade de votos, criando um índice que favorece o engajamento gerado no IMDb, mas sem desconsiderar a satisfação dos usuários em relação ao conteúdo.

A média utilizada foi: 

$$
\text{Média} = \frac{v}{v+m} \cdot R + \frac{m}{v+m} \cdot C ,
$$

onde:

- R é a média das classificações do título;
- v é o número de classificações do título;
- m é o mínimo de votos necessários para o título ser listado. Usaremos aqui a média truncada para darmos um maior peso ao número de votos. Eliminaremos os números de votos 10% mais baixos e os 10% mais altos e tiraremos a média;
- C é a média de todas as classificações.

## Conclusão:
Neste projeto, realizamos uma análise da popularidade dos títulos da Netflix disponíveis na plataforma IMDb. Nosso objetivo era entender como a popularidade é afetada por diferentes fatores, como avaliações, número de votos e tipo de conteúdo.

Para quantificar a popularidade, utilizamos uma fórmula de classificação ponderada que combina a avaliação média e o número de votos. Essa métrica foi formulada para dar mais importância ao número de votos, refletindo o engajamento gerado pelo título na plataforma. Utilizamos o teste de Mann-Whitney U para comparar a popularidade entre filmes e séries, e a mediana e o intervalo interquartil para descrever a distribuição da popularidade dentro de cada tipo de conteúdo.

Nossas conclusões foram as seguintes:

- Podemos avaliar a popularidade de um título observando as avaliações médias e a quantidade de votos. Isso nos permite criar uma ponderação que considera ambos os fatores em nossa análise, evitando distorções e dando mais peso ao engajamento gerado pelos títulos.

- Os títulos mais populares são, em geral, aqueles com as maiores avaliações médias e o maior número de votos.

- Quando pensamos em popularidade, as séries tendem a ser mais populares do que os filmes.

- Existe uma influência do tipo de conteúdo na popularidade. Há uma diferença estatisticamente significativa entre a popularidade dos filmes e das séries. As séries tendem a ser mais populares e apresentam uma maior variabilidade na popularidade. Isso pode indicar que os usuários preferem assistir e avaliar séries e que existe uma maior diversidade de opiniões entre elas.

Portanto, é possível criar um índice de popularidade que é influenciado por fatores como avaliação e número de votos. Os títulos mais populares são aqueles com as maiores avaliações médias e o maior número de votos, com um peso maior dado à quantidade de votos. As séries tendem a ser mais populares do que os filmes e também apresentam uma maior variabilidade na popularidade.
