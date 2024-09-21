### English Description

This project implements the classic "Dining Philosophers" problem using Python 🐍, showcasing the challenges of synchronization and resource sharing in concurrent programming 🤝. The implementation leverages object-oriented programming (OOP) principles to ensure clarity and maintainability ✨.

Key components include:

- **Class `Hashi`**: Represents chopsticks as individual objects 🍴. Each chopstick is managed using a semaphore to control access, ensuring that only one philosopher can use it at a time.

- **Class `Filosofo`**: Represents philosophers as threads 🧘‍♂️. Each philosopher alternates between thinking 💭 and eating 🍽️, encapsulating their behaviors in dedicated methods. The philosophers attempt to pick up the chopsticks on their left and right before eating, ensuring proper synchronization to avoid conflicts.

- **Synchronization**: The implementation effectively prevents deadlock 🚫 and starvation by managing the order in which chopsticks are acquired. Philosophers always pick up the lower indexed chopstick first, minimizing the chances of circular waiting.

This project serves as an educational example of concurrency, synchronization techniques, and the application of OOP principles in Python 🎓.

### Portuguese Description

Este projeto implementa o clássico problema dos "Filósofos à Mesa" utilizando Python 🐍, destacando os desafios da sincronização e do compartilhamento de recursos em programação concorrente 🤝. A implementação utiliza princípios de programação orientada a objetos (POO) para garantir clareza e manutenção ✨.

Componentes principais incluem:

- **Classe `Hashi`**: Representa os hashis como objetos individuais 🍴. Cada hashi é gerenciado utilizando um semáforo para controlar o acesso, garantindo que apenas um filósofo possa usá-lo por vez.

- **Classe `Filosofo`**: Representa os filósofos como threads 🧘‍♂️. Cada filósofo alterna entre pensar 💭 e comer 🍽️, encapsulando seus comportamentos em métodos dedicados. Os filósofos tentam pegar os hashis à sua esquerda e direita antes de comer, garantindo a sincronização adequada para evitar conflitos.

- **Sincronização**: A implementação previne efetivamente deadlock 🚫 e starvation ao gerenciar a ordem em que os hashis são adquiridos. Os filósofos sempre pegam o hashi de menor índice primeiro, minimizando as chances de espera circular.

Este projeto serve como um exemplo educacional de concorrência, técnicas de sincronização e a aplicação de princípios de POO em Python 🎓.
