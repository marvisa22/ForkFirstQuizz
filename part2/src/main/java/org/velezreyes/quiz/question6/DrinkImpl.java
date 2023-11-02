package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink{
    String name;

    public DrinkImpl(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        boolean isFizzy = false;
        if (name.equals("ScottCola")) {
            isFizzy = true;
        }else if(name.equals("KarenTea")){
            isFizzy = false;
        }
        return isFizzy;
    }
}
