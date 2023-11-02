package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
  double money = 0;

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    money += 0.25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if (money < 0.75 && name.equals("ScottCola") || money < 1 && name.equals("KarenTea")) {
      throw new NotEnoughMoneyException();
    }
    if(name.equals("ScottCola") || name.equals("KarenTea")){
      money = 0;
      return new DrinkImpl(name);
    }else {
      throw new UnknownDrinkException();
    }
  }
}
