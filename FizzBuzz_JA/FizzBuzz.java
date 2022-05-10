//Created by crisivanz1

import java.util.ArrayList;
import java.util.Scanner;

public class FizzBuzz 
{
    private final String fizz = "Fizz";
    private final String buzz = "Buzz";
    private final String fizzbuzz = fizz + buzz;
    private final int increment3 = 3;
    private final int increment5 = 5;

    public FizzBuzz()
    {

    }
    public void FBMenuSelect(ArrayList<String> Menu, Scanner input)

    {
        System.out.println("Welcome to the FizzBuzz program, Java Edition!");
        String[] Choices = {"1. One Player", "2. Two Players", "3. Vs the CPU", "4. Default"};

        int d;
        for (d = 0; d < Choices.length; d++)
            {
                System.out.println(Choices[d]);
            }

        String userInput = input.nextLine();

        while(true)
        {
            if (Menu.contains(userInput) != true)
            {
                System.out.println("Invalid input, please type something else!");
                userInput = input.nextLine();
            }
            else
            {
                switch(userInput)
                {
                    case "1":
                    {
                        FBOnePlayer();
                        break;
                    }
                    case "2":
                    {
                        FBTwoPlayers();
                        break;
                    }
                    case "3":
                    {
                        FBPlayerVsCPU();
                        break;
                    }
                    case "4":
                    {
                        FBDefault();
                        break;
                    }
                }
                break;
            }
        }
    }
   
    private void FBCPU(int i)
    {
        if (i % increment3 == 0 && i % increment5 == 0)
        {
            System.out.println(fizzbuzz);
        }
        else if (i % increment3 == 0)
        {
            System.out.println(fizz);
        }
        else if (i % increment5 == 0)
        {
            System.out.println(buzz);
        }
        else
        {
            System.out.println(i);
        }
        
    }
    private boolean FBPlayer(int i, Scanner input, Boolean failed)
    {
        String playerEntry = input.nextLine();
        if (i % increment3 == 0 && i % increment5 == 0)
        {
            if (playerEntry.toUpperCase().equals(fizzbuzz.toUpperCase()) == false)
                failed = true;
        }
        else if (i % increment3 == 0)
        {
            if (playerEntry.toUpperCase().equals(fizz.toUpperCase()) == false)
                failed = true;
        }
        else if (i % increment5 == 0)
        {
            if (playerEntry.toUpperCase().equals(buzz.toUpperCase()) == false)
                failed = true;
        }
        else
        {
            if (playerEntry.equals(String.valueOf(i)) == false)
                failed = true;
        }
        return failed;
    }
    private String FBFailState()
    {
        return "\nWhoops, wrong answer. You lose!";
    }
    private String FBFailState(boolean playerTurn)

    {
        if (playerTurn)
        {
            return "\nWhoops, wrong answer. Player 1, You lose!\nPlayer 2, you win!";
        }
        else
            return "\nWhoops, wrong answer. Player 2, you lose!\nPlayer 1, you win!";
    }
    private void FBOnePlayer()
    {
        boolean failed = false;
        Scanner input = new Scanner(System.in);
        int i;

        System.out.println("Hello player! Hope you know how to play FizzBuzz!");
    
        for (i = 1; i <= 100; i++)
        {
            failed = FBPlayer(i, input, failed);
            if (failed)
            {
                System.out.println(FBFailState());
                break;
            }
        }
        if (failed != true)
            System.out.println("You win!");

        System.out.println("Thank you for playing FizzBuzz!");
    }
    private void FBPlayerVsCPU()

    {
        boolean failed = false;
        Scanner input = new Scanner(System.in);
        int i;
        boolean playerTurn = true;

        System.out.println("Hello player! Hope you know how to play FizzBuzz! Today your opponent is a machine!");
    
        for (i = 1; i <= 100; i++)
        {
            if (playerTurn)
            {
                failed = FBPlayer(i, input, failed);
                if (failed)
                {
                    System.out.println(FBFailState());
                    break;
                }
                playerTurn = false;
            }
            else
            {
                FBCPU(i);
                playerTurn = true;
            }
        }
        System.out.println("Thank you for playing FizzBuzz!");
    }
    private void FBTwoPlayers()
    {
        boolean failed = false;
        Scanner input = new Scanner(System.in);
        int i;
        boolean playerTurn = true;

        System.out.println("Hello players! Hope you know how to play FizzBuzz! Today your opponent is each other! !");
    
        for (i = 1; i <= 100; i++)
        {
            if (playerTurn)
            {
                System.out.println("Player 1, your turn: ");
                failed = FBPlayer(i, input, failed);
                if (failed)
                {
                    System.out.println(FBFailState(playerTurn));
                    break;
                }
                playerTurn = false;
            }
            else
            {
                System.out.println("Player 2, your turn: ");
                failed = FBPlayer(i, input, failed);
                if (failed)
                {
                    System.out.println(FBFailState(playerTurn));
                    break;
                }
                playerTurn = true;
            }
        }
        System.out.println("\nThank you for playing FizzBuzz!");
    }
    private void FBDefault()
    {
        int i;
        for (i = 1; i <= 100; i++)
        {
            FBCPU(i);
        }
    }

    public static void main(String[] args) 
    {

        FizzBuzz FB = new FizzBuzz();
        Scanner input = new Scanner(System.in);

        ArrayList<String> MenuChoices = new ArrayList<String>(4);
        MenuChoices.add("1");
        MenuChoices.add("2");
        MenuChoices.add("3");
        MenuChoices.add("4");

        FB.FBMenuSelect(MenuChoices, input);

    }   
}



