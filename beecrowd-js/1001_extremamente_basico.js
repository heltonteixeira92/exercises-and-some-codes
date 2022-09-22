/*
PROBLEMA:1001 - Extremamente Básico
RESPOSTA:Accepted
LINGUAGEM:JavaScript (nodejs 8.4.0) [+2s] {beta}
TEMPO:0.633s
TAMANHO:302 Bytes
MEMÓRIA:-
SUBMISSÃO:21/07/2022 19:41:45
 */
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

/**
 * Escreva a sua solução aqui
 */

var a = parseInt(lines.shift());
var b = parseInt(lines.shift());

console.log('X = ' + (a+b));