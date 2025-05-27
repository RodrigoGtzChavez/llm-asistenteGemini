
# ✍️ Asistente de Escritura Inteligente con Gemini (Versión Simple)

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-lightgrey.svg)](http://unlicense.org/)

Este proyecto es una **versión inicial y simplificada** de un Asistente de Escritura inteligente.

Aprovecha el poder de la API de **Google Gemini** para ofrecerte sugerencias de estilo, corrección gramatical y generación de texto, todo ello accesible a través de una interfaz web intuitiva.

<br>

✨ **Características (Versión Simple):**

* 📝 **Editor de Texto Básico:** Un área de texto (textarea) intuitiva para que puedas escribir y editar tu contenido fácilmente.
* ✨ **Mejora de Texto:**
    * Envía tu texto a Gemini para recibir **correcciones gramaticales**, **sugerencias de estilo**, y mejoras para una mayor **claridad y concisión**.
* 💡 **Completado de Texto:** Permite que Gemini genere continuaciones lógicas para tus oraciones o párrafos, una herramienta ideal para **desbloquear tu creatividad** y superar el bloqueo del escritor.
* 🌐 **Interfaz Simple:** Una aplicación web **ligera y fácil de usar**, construida con las tecnologías web fundamentales: **HTML**, **CSS** y **JavaScript**.

<br>

## ⚙️ Arquitectura del Sistema (Conceptual)

Aunque esta es una versión simple, la arquitectura conceptual detrás de un sistema de asistente de escritura más completo podría verse así:

```mermaid
graph LR
    A --> D(Módulos de Vista: Editor);

    subgraph Frontend
        direction LR
        A
        C
        D
    end

    E[Backend (Servicios Core)] --> F(Servicio de Autenticación/Usuarios);
    E --> G(Servicio de Proyectos/Documentos);
    E --> H(Servicio de Procesamiento de Texto - NLP);
    E --> I(Servicio de Generación de Contenido);
    E --> J(Servicio de Almacenamiento de Archivos);

    subgraph Backend
        direction LR
        E
        F
        G
        H
        I
        J
    end

    K[Base de Datos de Usuarios (Auth)] <-- F;
    L[Base de Datos de Proyectos/Documentos] <-- G;
    M[Base de Datos de Configuración/Modelos] <-- I;
    J --> N[Almacenamiento de Archivos (Opcional)];

    subgraph Bases de Datos
        direction LR
        K
        L
        M
        N
    end

    O[API de Google Gemini] <-- I & H;
    P[Modelos NLP Custom] <-- H;
    Q[Servicio de Detección de Plagio (Terceros)] <-- H;

    subgraph Servicios Externos / ML
        direction LR
        O
        P
        Q
    end

    style Frontend fill:#f9f,stroke:#333,stroke-width:2px
    style Backend fill:#ccf,stroke:#333,stroke-width:2px
    style "Bases de Datos" fill:#9cf,stroke:#333,stroke-width:2px
    style "Servicios Externos / ML" fill:#fcc,stroke:#333,stroke-width:2px
