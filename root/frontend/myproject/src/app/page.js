import Image from "next/image";

export default function Home() {
  return (
    <main>
    <body>
        <header>
            <h1>Freestyle Buddy</h1>
            <nav>
                <ul>
                    <li><a href="{% url 'home' %}">Home</a></li>
                    <li><a href="{% url 'studio' %}">Studio</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <div>
                <label for="topicInput">Enter your topic:</label>
                <input type="text" id="topicInput" name="topic"></input>
                <button id="generateBtn">Generate Lyrics</button>
            </div>
            <div id="lyricsOutput"></div>
        </main>
    
    </body>
    </main>
  );
}
