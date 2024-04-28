# Docker Con
Docker Container Übungen in SW 09 für Lernjournal im Modul DevOps

Follow instruction on: https://hub.docker.com/r/ollama/ollama

Main steps to get started:

1. Pull and run docker from Docker Hub:

## CPU Only
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## Run model locally
```
docker exec -it ollama ollama run llama2
docker exec -it ollama ollama run mistral
```

More models from [Ollama library](https://ollama.com/library) can be found on the official website.

## How to use? 
Directly write your promt into the console. Example of model [llama2] (https://ollama.com/library/llama2) below:

### Prompt: 
>>> *Why is the sky blue?*

### Anwer: 
*"The sky appears blue because of a phenomenon called Rayleigh scattering. When sunlight enters Earth's atmosphere, it encounters tiny molecules of gases such as
nitrogen and oxygen. These molecules scatter the light in all directions, but they scatter shorter (blue) wavelengths more than longer (red) wavelengths. This is        
known as Rayleigh scattering.

As a result of this scattering, the blue light is dispersed throughout the atmosphere, giving the sky its blue appearance. The blue color becomes more pronounced        
in the morning and evening when the sun is lower in the sky, because the light has to travel through more of the Earth's atmosphere to reach our eyes.

It's worth noting that the color of the sky can vary depending on the time of day, weather conditions, and even the location on Earth. For example, during sunrise       
and sunset, the sky may take on hues of red, orange, and pink due to the angle of the sunlight and the scattering of light by atmospheric particles.

In summary, the sky appears blue because of Rayleigh scattering, which disperses blue light throughout the atmosphere, giving it a blue appearance."*