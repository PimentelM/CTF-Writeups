In this challange we recieved a binary called primes. After opening it on a disassembler we could quickly see that the binary was recieving a stream of bytes, writing them to executable memmory mapped at 0x1337000 and, if all bytes of the stream were primes, the execution would jump to that location.

So our goal was to write a piece of shellcode whose bytes where all prime numbers.

First of all, i went to <a href="http://ref.x86asm.net/coder64.html">this</a> website and wrote a piece of javascript to highlight all lines with prime opcodes.

<div>
  <img src="opcodes.png" width="50%" style="display: inline">
  
  <img src="opcodes2.png" width="45%" style="display: inline">  
</div>

XOR, OR, AND , ADD, SUB, MOV, IMUL , ROT.

And i also mapped all register opcodes that were primes: 

![notepad](notepad.jpeg)

Then i started to create a strategy based on which operations we had avaliable.

I decided that my strategy would be this one:

1- Transform a standard shellcode into a series of DWORDS. ( I used python's struct.unpack function. )

![dwords](dwords.png)

2- Mov every dword to a location at the end of the prime-number-made-shellcode.

Basically, we would do something like this, but using only prime numbers:
<pre>
MOV EAX, 0x1337000
ADD EAX, SIZE_OF_THIS_SHELLCODE
MOV EDI, EAX
MOV EAX, FIRST_DWORD_OF_THE_ACTUAL_SHELLCODE
MOV [EDI] , EAX
INC EDI, 4
MOV EAX, SECOND_DWORD_OF_THE_ACTUAL_SHELLCODE
MOV [EDI], EAX
INC EDI, 4
[...]
</pre>
And we would do this until all dwords were placed at the end of the shellcode. So when we finish executing it, the program would execute our arbitrary code and we would get a shell.

So, with that in mind i started making my set of instructions using python variables to store the opcodes inside representative names.

![instructions](instructions.png)

The trickiest part was to make an arbitrary mov eax , value. But the solution i came with was amazingly elegant imo =]

The number was bit by bit set using bitwise and bitshift operations. ( i used imul edi, 2 to simulate a shl edi, 1 )

Then, when everything was done, i just made the shellcode, debugged it, and voilà, we had arbitrary shellcode execution and got the flag! =]
_________________________


I will be postiong the final script as it is, without changes, this is why there is some portuguese text and the "ADD EAX, SIZE_OF_THIS_SHELLCODE" part of the shellcode is awkward ( a lot of ADD_EBX_BY(101) instructions that i could replace by a single MOV_EAX_DWORD ; MOV_EBX_EAX . ). This is because as always happens in CTF, i got the flag before changing that code







