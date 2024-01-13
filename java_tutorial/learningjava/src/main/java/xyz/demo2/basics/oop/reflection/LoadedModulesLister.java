package xyz.demo2.basics.oop.reflection;


import java.lang.module.ModuleReference;
import java.util.Set;

public class LoadedModulesLister {
    public static void main(String[] args) {
        // Get the current module layer
        ModuleLayer layer = ModuleLayer.boot();

        // Get the set of modules in the current layer
        Set<Module> modules = layer.modules();

        // Iterate through the modules and print their names
        for (Module module : modules) {
            System.out.println("Module Name: " + module.getDescriptor().name());
        }
    }
}
