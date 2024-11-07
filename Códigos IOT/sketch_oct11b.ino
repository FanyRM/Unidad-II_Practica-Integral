/*  ----------------------------------------------------------------
Fco. Javier Rodriguez Navarro   www.pinguytaz.net
  
Generando musica
 
------------------------------------------------------------------*/

// Descomenta la melodia que desees
//#include "FrereJacques.h"
#include "GGalaxia.h"


   #define BZ 18


void setup()  // configuracion placa
{
   // También cambiaríamos la velocidad del puerto de consola segun plataforma
   pinMode(BZ, OUTPUT);


      Serial.begin(115200);
}

void loop()  //Se repite indefinidamente,
{
  Serial.print("Inicio Melodia --- ");
  for (int i=0 ; i < NOTAS; i++)
  {
     beep(duracion[i],melodia[i]);
  }
 
  Serial.println("FIN");
  delay(1500);
}


/************************************************************
 * Funciones para generar sonido
 * 
 * void beep(float, unsigned int tono)  
 *    Genera una nota indexada como 0 el DO de la 4ª Octava
 *    de una duración.
 *    La Nota 100 Indica silencio
  ************************************************************/
void beep(float duracion, unsigned int nota)
{
   int frecuencia;  

   if(nota < 100)
   {
      // Calculamos la frecuencia a tocar, indice 0 Do4
      frecuencia = (int) 261.625 * pow(1.0594630943593,nota);
   }
   else frecuencia =0;
   
      frecuencitone(BZ,a);
     delay(duracion*500);
     noTone(BZ);
}