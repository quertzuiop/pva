using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;


class Program
{
    static void Main(string[] args)
    {
        Game game = new Game();
        Dice dice1 = new Dice();
        Dice dice2 = new Dice();
        while (true)
        {
            var inputStr = Console.ReadLine();
            if (inputStr == "exit") break;
            var input = inputStr.Split(" ");
            if (input[0] == "add")
            {
                if (input.Length != 2)
                {
                    Console.WriteLine("Incorrect number of arguments");
                    continue;
                }
                game.AddPlayer(input[1]);
                Console.WriteLine("Added player " + input[1]);
            }
            else if (input[0] == "play")
            {
                if (input.Length == 1) game.PlayAll();
                else for (int i = 0; i < int.Parse(input[1]); i++)
                {
                    game.PlayAll();
                }
            }
            else if (input[0] == "won")
            {
                Console.WriteLine(game.HasPlayerWon(input[1]));
            }
            else if (input[0] == "scores")
            {
                game.PrintScores();
            }   
        }
    }
}
class Dice
{
    public Dice(){ }
    public int Roll()
    {
        Random rnd = new Random();
        return rnd.Next(1, 7);
    }
}   
class Player
{
    public string Name { get; set; }
    public int Score { get; set; }
    public Player(string name)
    {
        Name = name;
        Score = 0;
    }
    public (int, int) Roll(Dice dice1, Dice dice2)
    {
        return (dice1.Roll(), dice2.Roll());
    }
    public void UpdateScore(int r1, int r2)
    {   
        if (r1 == 1 && r2 == 1)
        {
            Score = 0;
        }
        else if (r1 == 1 || r2 == 1) return;
        else
        {
            Score += r1 + r2;
        }
    }
}   
class Game
{
    public List<Player> Players { get; set; }
    private Dice dice1 = new Dice();
    private Dice dice2 = new Dice();
    private string? lastPlayer;
    public Game()
    {
        Players = new List<Player>();
    }
    public void AddPlayer(string name)
    {
        Players.Add(new Player(name));
    }
    public void PlayAll()
    {
        if (PlayerCountIncorrect())
        {
            Console.WriteLine("Incorrect number of players");
            return;
        }
        foreach (var player in Players)
        {
            var (r1, r2) = player.Roll(dice1, dice2);
            player.UpdateScore(r1, r2);
            if (HasPlayerWon(player.Name))
            {
                Console.WriteLine(player.Name + " has won!");
                return;
            }
            lastPlayer = player.Name;
        }
    }
    public void PlayOne()
    {
        if (PlayerCountIncorrect())
        {
            Console.WriteLine("Incorrect number of players");
            return;
        }
        var player = Players.First(p => p.Name == lastPlayer);
        var (r1, r2) = player.Roll(dice1, dice2);
        player.UpdateScore(r1, r2);
    }
    public bool HasPlayerWon(string name)
    {
        return Players.First(p => p.Name == name).Score >= 100;
    }
    public void PrintScores()
    {
        foreach (var player in Players)
        {
            Console.WriteLine($"{player.Name}: {player.Score}");
        }
    }
    private bool PlayerCountIncorrect()
    {
        return Players.Count < 2 || Players.Count > 5;
    }
}