import random
from os import system

def clear():
	system("clear")

def banner():
	print("""\033[1;33m
 *******     **    *     *          ****   ****  ****     **
/**////**   */*  ***** *****       */// * */// */**/**   /**
/**   /**  * /* /*/*/ /*/*/       /*   / /    /*/**//**  /**
/*******  ******/*****/***** *****/*****    *** /** //** /**
/**////  /////* ///*/*///*/*///// /*/// *  /// */**  //**/**
/**          /*  ***** *****      /*   /* *   /*/**   //****
/**          /* ///*/ ///*/       / **** / **** /**    //***
//           /    /     /          ////   ////  //      ///\033[0m
\033[41m Password Generator | https://github.com/t0mxplo1t \033[0m""")

def Generate_Password(num):
    password = ''

    for n in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
    return password


print(Generate_Password(16))