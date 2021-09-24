/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.alittleaesthetic.co.kittentype;

/**
 *
 * @author joshua
 */
public class Stats {
    public int xp;
    public int hp;
    public int age;
    
    public Stats(Stats other){
        this(other.xp, other.hp, other.age);
    }
    
    public Stats(int xp, int hp, int age){
        this.xp = xp;
        this.hp = hp;
        this.age = age;
    }
}
