/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package co.alittleaesthetic.co.kittentype;

import java.util.Map;

/**
 *
 * @author joshua
 */
public class pets {
    public enum PetClass {BABY, ADULT}
    
    Map<PetClass, Stats> classToStats = Map.of(PetClass.BABY, new Stats(10,10,10), PetClass.ADULT, new Stats(10,10,10));
    
    public String name;
    public PetClass petclass;
    public Stats stats;
    
    public pets(String name, PetClass petclass){
        this.name = name;
        this.petclass = petclass;
        
        this.stats = new Stats(classToStats.get(petclass));
    }
}
