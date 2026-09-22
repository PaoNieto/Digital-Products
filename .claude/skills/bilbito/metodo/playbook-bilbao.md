# Playbook de Santi Bilbao: la mecánica completa

Santi Bilbao escala productos digitales de ticket bajo con anuncios de Meta. Este archivo es su mecánica,
destilada de su curso de Meta Ads (17 clases) y de 248 videos de su canal, más dos correcciones de Claudio
Conde, que da clases en el mismo curso.

## Cómo leer este archivo

- **Se toma la mecánica, nunca el copy.** Sus guiones prometen ingresos ("pasé de 300 a 3 mil"). Eso viola
  las políticas de Meta. Se queda el esqueleto; el claim se tira.
- **Todos los números son de Santi Bilbao, no verificados para Paolo.** Salen de sus cuentas (Argentina,
  EE. UU., España). Sirven como método, no como umbral. Los de Paolo salen de testear.
- Todo gasto en anuncios espera la compuerta del `SKILL.md`: 10 de 10 ventas a desconocidos en `CLAUDE.md`.
- Toda cuenta usa lo que **deja** la venta (está en `CLAUDE.md`), nunca el precio de lista. Donde Bilbao dice
  "ticket" o "facturación", acá se lee "lo que deja".
- Montos en dólares con su equivalente en soles al supuesto de trabajo de S/3.7 por dólar (chequear el día).

---

## 1. La ecuación madre

```
costo por visita (CPV)  <  lo que deja cada visita (RPV)   →   rentable. Punto.
```

- CPV = gasto ÷ visitas que cargaron la página.
- RPV = lo que dejan las ventas ÷ visitas.
- Todo el trabajo es bajar el CPV o subir el RPV. Todas las otras métricas alimentan una de las dos.

**La cadena completa**, de arriba hacia abajo:

```
impresiones → CTR → clic en el enlace → % de carga → visita → % de conversión → compra → costo por comprador vs techo
```

**CPV no es CPC.** El CPC es lo que cuesta el clic; el CPV, lo que cuesta una visita que de verdad vio la
página. La diferencia es el % de carga, y ahí la plata se evapora en silencio.

## 2. Los tres números que mandan

| Número | Qué es | Regla |
|---|---|---|
| Techo por comprador | Lo que deja una venta, en dólares. Acá lo da Mercaneto | Todo costo por comprador por encima se corta. Sin apego |
| Costo por visita | La métrica que valida la **oferta**. Se ve el primer día | Si desde el día 1 o 2 no entra más de lo que sale, la oferta no es |
| Conversión de la página | compras ÷ visitas, con los datos de Whop, no los de Meta | Bilbao: más de 2.5 a 3%. Por debajo no se escala: primero la página |

### Validar la oferta: la cuenta de Bilbao

Su ejemplo, con un producto que deja US$15 y 2 compras cada 100 visitas (sus números):

| Costo por visita | 100 visitas cuestan | Entran (2 × US$15) | Veredicto |
|---|---|---|---|
| 15 centavos de dólar | US$15 | US$30 | Gana el doble: escalar |
| 30 centavos de dólar | US$30 | US$30 | Empate: no se gana nada |
| 1 dólar | US$100 | US$30 | Haría falta 7% de conversión: "es inhumano". Matar o cambiar creativo |

Para Paolo, la misma cuenta con N (lo que deja su venta, del `CLAUDE.md`): con 2 de cada 100, el techo por
visita es N ÷ 50. Su conclusión: **es más fácil bajar el costo por visita que subir la conversión.** Por eso
invierte en hacer buenos anuncios antes que en retocar la página.

## 3. Umbrales de buen anunciante

| Métrica | Umbral de Bilbao | Qué mueve |
|---|---|---|
| Hook rate (reproducciones de 3 s ÷ impresiones) | más de 50% | Sube el CTR |
| Retención (base no definida por él; supuesto: reproducciones completas ÷ impresiones) | más de 10% | Sube el CTR |
| CTR del enlace | 2 a 3%; los ganadores, más de 3% | Baja el CPC |
| Carga de la página | más de 70% (Conde: ideal 85 a 95%) | Baja el CPV |
| Ticket promedio ÷ precio de entrada | 1.5, con productos detrás | Sube el RPV |

Con CTR de 4% en vez de 2%, las mismas impresiones dan el doble de clics: el clic cuesta la mitad.

## 4. El test de un producto nuevo

**Siempre ABO para lo nuevo.** Bilbao a veces testea en CBO (una canilla para todo el jardín); Conde dice que
nunca, porque en CBO Meta decide dónde gasta y no sabés qué funcionó. Con presupuesto chico, saber qué funcionó
vale más que la eficiencia: gana Conde.

Lanzamiento de validación de Bilbao: 1 campaña, 6 conjuntos (3 con foto, 3 con video), 1 anuncio por conjunto,
US$6.50 por conjunto por día (unos S/24).

### Armado paso a paso

| Paso | En el Administrador de anuncios | En Whop Ads (docs de Whop, 21/09/2026) |
|---|---|---|
| Objetivo | Ventas | objective: sales |
| Presupuesto | A nivel conjunto (ABO). Apagar el de campaña | budget_optimization: ad_group (es el default) |
| Conversión | Sitio web, nunca mensajes | conversion_location: website |
| Optimización | Maximizar el número de conversiones | optimization_goal: conversions |
| Evento | Compra (puede figurar inactivo en la primera campaña) | conversion_event: purchase. Whop lo registra solo si la compra pasa por su checkout |
| Plata | US$5 a 10 por conjunto (S/19 a 37) | budget_amount, budget_type: daily |
| Programación | 00:00 del día siguiente, siempre | — |
| Fin | Ninguno. Se apaga a mano | ends_at vacío |
| Segmentación | País, idioma y edad. Todo lo demás abierto | languages, demographics.minimum_age: 18, demographics.automatic: false |
| Formato | Una imagen o un video por anuncio. Apagar "anuncios multi-anunciante" | — |
| Título | Copy del anuncio. El "4.9 de 5" de Bilbao, solo si es el promedio real de reseñas | — |
| Mejoras con IA | Apagar todas | dynamic_creative: Meta ya no lo acepta |
| Nombres | Campaña `testeo - [fecha] - [producto]`; conjunto `[fecha] - [nro de creativo]` | title |

- Para 5 anuncios: se arma el primer conjunto completo y se duplica 4 veces. Solo cambia el creativo.
- Solo dos campañas de test en toda la cuenta; mañana se agregan conjuntos adentro de la misma.
- Columnas que se miran: resultados, costo por resultado y **valor promedio de compra**. Sin la última se
  matan conjuntos rentables cuando hay productos detrás que suben el ticket.
- Nunca imágenes y videos en el mismo conjunto: no sabés de dónde vino el resultado.
- Un test dura de 12 a 72 horas. Nunca más de 72.
- Programado a las 00:00 → se revisa a las 12 h (se apagan los malos) → se revisa a las 48 h. De 10 anuncios
  suelen quedar unos 3.
- Si la campaña no gasta nada: presupuesto demasiado bajo o primera campaña de la cuenta.

## 5. Las reglas de corte

**Antes de decidir, el anuncio tiene que gastar cerca del techo por comprador.** "Si no gastó eso, no tomes
decisiones. Acá es muy importante controlar las emociones."

| Escenario | Ejemplo de Bilbao (techo US$14) | Qué hacés |
|---|---|---|
| Vendió bien | Gastó 14, hizo 3 ventas | Dejar correr. Mirar a diario que no pase el techo |
| Vendió 1 | Gastó 14, una venta | Darle US$1 a 2 más (S/4 a 7). Si gasta 2 o 3 más sin vender, apagar |
| No vendió | Gastó 12 o 13, sin carritos ni pagos iniciados | Cortar. Que nadie inicie el pago es señal temprana |

**Tirón de oreja**, en vez de matar: si el costo se encarece, bajar 30% el presupuesto. Si al otro día
recupera, se sube de nuevo. Siempre mirando los últimos 3 a 4 días.

> "Tu misión no es qué campaña tirar, sino cuándo apagar a tiempo."

## 6. El pre-test: solo para ofertas que ya escalan

Filtrar creativos por CPC antes de darles plata de test: 30 creativos por día (20 imágenes, 10 videos) a
US$1.50 a 2 cada uno (S/6 a 7), corren 21 horas y se apagan todos. Pasan al test los que tienen CPC por debajo
del promedio de la cuenta, más los que vendieron.

La cuenta del ahorro: de 30 creativos, unos 25 no andan. Tirarlos directo al test a US$15 quema unos US$375;
pre-testearlos a US$2 cuesta unos US$60.

**Para un producto nuevo, no.** Obliga a Meta a conseguir una venta con centavos, y con ticket bajo es
imposible. Producto nuevo → test directo a US$5 a 10 por conjunto.

## 7. Qué es un ganador

| Es ganador | No es ganador |
|---|---|
| Generó ventas bajo el techo | Likes, cero ventas |
| CPC más bajo que el promedio de la cuenta | CPC alto |
| CTR alto | Muchas impresiones, nadie entra |
| Funcionó en las primeras 72 h | "Se ve lindo pero no genera nada" |

Umbral para escalar: **10 ventas o más** a buen costo (confiable); 6, aceptable; 3 o 4 en los últimos 7 días,
"buena pinta" para probar un fin de semana. Excepción: si a las 2 horas ya metió 2 o 3 ventas, puede pasar
directo a tope de costo.

**Regla de oro: nunca se escala lo que no demostró ser ganador en el test.**

## 8. Escalar

### Vertical
Esperar 3 días y 7 a 10 compradores, después +15% por día al conjunto. Si subís y al otro día no vende, no
subas de nuevo. La versión del resumen de su canal: +25 a 30% por día mientras lo que entra sea 1.5 veces lo
gastado, o el doble cada 2 horas en modo agresivo.

Vida útil de un escalado agresivo: unos 3 días. Después se quema; es normal. El ganador se exprime y se pasa
a la campaña estable.

### Cuándo
Viernes a domingo. Con tickets bajos la gente compra por impulso, scrollea más y no está trabajando. Es la
recomendación que más se repite en todo el curso. De lunes a jueves, se testea.

### Estructuras (todas con anuncios ya ganadores)

| Estructura | Anuncios | Conjuntos | Plata |
|---|---|---|---|
| CBO de ganadores | 3 a 5 ganadores distintos | 1 por ganador | 5 campañas iguales a 30, 40, 50, 60 y 70 dólares por día, "para ver cuál agarra viaje" |
| CBO aislada | 1 ganador repetido | 3 | mínimo US$30 por día |
| CBO pocket | 1 ganador repetido | 8 | mínimo US$30 por día |
| Tope de costo | Hasta 5 ganadores distintos por conjunto | ABO, 1 campaña | Arranca alto; no lo gasta si no consigue el costo |
| Micro-presupuesto | El mismo ganador en todos | 10 a 20, ABO | US$2.75 a 3 por conjunto. Para pescar compras regaladas |

Por qué duplicar conjuntos idénticos: cada uno recibe una porción distinta de la audiencia. Es tirar 10
líneas al agua en vez de una.

### Tope de costo: la del pico
Campaña ABO donde le decís a Meta cuánto pagás por compra; si no lo consigue, no gasta.

- 7 conjuntos con el **mismo** anuncio ganador, US$15 a 25 por conjunto.
- Escalera de pujas con el medio un poco arriba de tu costo promedio: `4 · 5 · 6 · [7] · 8 · 9 · 10`.
  Si el producto vale unos US$19, el medio va en 9: `6 · 7 · 8 · [9] · 10 · 11 · 12`.
- Si en 2 días no arranca ninguno, se sube toda la escalera.
- Se mira 4 veces por día: a la mañana se duplica el que vendió y se corta el que no arrancó; al mediodía y a
  la tarde, si sigue vendiendo, se duplica; a la noche se vuelve todo al presupuesto base.
- No es para vender parejo: es para hacer pico en días buenos. Su dato: de 49 conjuntos, un domingo arrancó uno
  solo y metió 15 compras. Otros días no arranca ninguno.

En Whop Ads: bid_type `average_target` es apuntar a un costo promedio (tope de costo) y `maximum_target`, no
pasar nunca de un costo (límite de puja), con desired_cost_per_result. El tope por ROAS no figura en la
documentación de Whop al 21/09/2026.

### Las pujas de Meta

| Estrategia | Qué le decís a Meta | Cuándo |
|---|---|---|
| Volumen más alto (la de fábrica) | "Conseguime lo máximo". Gasta todo sin mirar el costo | Test y campaña estable |
| Objetivo de costo por resultado | "No pago más de X por venta; si no, no entres a la subasta" | Escalar |
| Objetivo de ROAS | Lo mismo, pero con retorno en vez de costo | Escalar con productos detrás |
| Límite de puja | Máximo a pujar en la subasta | Avanzado |

Cómo elegir la puja inicial: mirá el costo por resultado promedio de toda tu data. Si da 7 y tu techo es 15,
arrancá en 10. Con 7 exacto puede no arrancar.

### El surfeo: escalar dentro del mismo día

| Situación | Acción |
|---|---|
| Arrancó y vende a buen costo | Duplicar presupuesto y estirar la puja hasta el techo. Abrirle la canilla |
| Sigue vendiendo bien | Seguir duplicando. La puja no se toca |
| El costo sube | Bajar la puja. Puede frenar; no pasa nada |
| Dejó de gastar pero cerró a buen costo | Subir la puja |
| El costo se dispara | Apagar. Mañana es otro día |
| No arranca a la mañana | Subir la puja de a 1, con 1 hora entre cada suba |
| A la noche | Volver a lo original (si arrancó recién en 12, volver a 12, no a 10) |

Llevar un registro diario: qué pasa los martes, los sábados, a qué puja arrancó y a qué hora. "La ambición es
un arma del diablo: si te metió 10 ventas, no estés desagradecido."

El surfeo exige ver las ventas casi en vivo: el pixel suele atrasarse entre 30 minutos y 1 hora, y se termina
apagando lo que sí vendía. Recién tiene sentido con volumen.

## 9. La fase de aprendizaje y la campaña estable

- Un conjunto sale de aprendizaje con más de 50 compras en menos de 7 días. "Un conjunto con 50 compras es
  una biblioteca de 50 personas que compraron: necesita más presupuesto, nada más."
- La campaña estable arranca perdiendo plata los días 1 a 3; del 4 al 7 Meta encuentra a quién venderle.
  **El error más caro: apagarla en esos primeros días.**
- **La campaña estable no se toca.** Ni creativos nuevos ni cambios de presupuesto: cada cambio le borra lo
  aprendido. Se hace una vez y se deja. Todo el movimiento va en test y escalado.
- En la estable no se surfea; como mucho, +20% por día.

## 10. El combustible: creativos nuevos todo el tiempo

- De 10 creativos salen 1 o 2 ganadores. Si se deja de testear, los ganadores se queman y no hay reemplazo.
- Error clásico: llegar a vender bien y relajarse.
- Por campaña: 2 ganadores probados más 2 nuevos que no se parezcan en nada.
- Bilbao habla de 50 creativos por día. Es su escala, no la de Paolo: con pocas horas por semana, lo que
  importa es la cadencia (ángulos nuevos 2 o 3 veces por semana, el resto variaciones del que ya vende).

## 11. Elegir países por RPV (cuando ya hay volumen)

1. Ventas por país en Whop ÷ visitas por país = lo que deja cada visita, por país.
2. En Meta: costo por clic con desglose por país.
3. Se quedan los países donde lo que deja la visita supera lo que cuesta. Los demás, afuera.

Su dato, con un costo por visita de US$0.20: EE. UU. dejaba US$0.62 por visita y con volumen real; México,
apenas arriba del costo; Argentina, US$0.10: "estoy perdiendo, por eso no corro ahí". Dice que Perú "no compra
mucho, depende del producto". Todo no verificado.

Arranca amplio por regiones y después poda con datos.

## 12. Elegir la oferta: funnel hacking

Lo ejecuta El Gato; Bilbito usa lo que trae.

- No inventar: modelar lo que ya escala. Palabras clave del texto de anuncios ajenos + Biblioteca de Anuncios.
- Señales: anuncio con más de 3 días corriendo (filtra a los que solo testean) y 7 o más creativos activos
  (señal de que escala).
- Desarmar lo que venden detrás de la compra: segundo producto al pagar, oferta después de la compra,
  versión más barata al que dice que no, suscripciones.

## 13. El modelo de negocio de Bilbao

- Venta directa todo el año, no lanzamientos.
- Producto de entrada barato que paga el anuncio, más productos detrás que suben el ticket. Objetivo: ticket
  promedio 1.5 veces el precio de entrada.
- **La tesis de la subasta:** el que deja más por visita puede pagar más por cada clic y aguanta cuando el
  anuncio se encarece. Los productos detrás no son un extra: son la defensa.
- Qué productos van detrás y a cuánto lo deciden Mercaneto y el-panadero, no Bilbito.

## 14. Medir sin creerle todo al panel

- Un estudio con 663 experimentos reales en Facebook (Gordon, Moakler y Zettelmeyer) encontró que los
  métodos habituales de atribución sobreestiman el efecto de los anuncios en compras varias veces.
- Regla: no se escala solo con el número del panel de Meta. Se cruza con las ventas que registra Whop.
  Según la documentación de Whop, sus reportes de compras y retorno cuentan solo los pagos que procesó Whop.

## 15. TikTok

No hay material de Bilbao específico de TikTok. La mecánica se traslada (CPV contra RPV, presupuesto por grupo
de anuncios para testear, reglas de corte, un cambio por vez); los umbrales no. Antes de gastar ahí: leer sus
políticas y verificar que la compra de Whop le llegue al pixel de TikTok. Nada de eso está verificado al
21/09/2026.

## 16. Prácticas del curso que NO se copian

1. Reseñas falsas en el checkout.
2. Testimonios inventados para arrancar.
3. Compra de seguidores para que el perfil no parezca fantasma.
4. El "4.9 de 5" en el título sin reseñas reales detrás.
5. Escasez que no existe ("quedan 5 cupos" de un archivo que no se acaba).

Son contenido fabricado: violan las políticas de Meta y la ley de defensa del consumidor. La alternativa
legítima está en el mismo curso: dar acceso gratis a gente del nicho a cambio de un testimonio real, y pedirlo
con insistencia.
