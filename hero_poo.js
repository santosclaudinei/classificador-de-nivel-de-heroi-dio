class Hero {
    constructor(name, age, type) {
      this.name = name;
      this.age = age;
      this.type = type;
    }
  
    attack() {
      let attack;
      switch (this.type) {
        case "mage":
          attack = "used magic";
          break;
        case "warrior":
          attack = "used sword";
          break;
        case "monk":
          attack = "used martial arts";
          break;
        case "ninja":
          attack = "used shuriken";
          break;
        default:
          attack = "used an undefined attack";
      }
  
      console.log(`The ${this.type} attacked using ${attack}`);
    }
  }
  
  // Example of usage
  const hero1 = new Hero("Gandalf", 1000, "mage");
  hero1.attack();
  
  const hero2 = new Hero("Aragorn", 35, "warrior");
  hero2.attack();
  
  const hero3 = new Hero("Bruce Lee", 33, "monk");
  hero3.attack();
  
  const hero4 = new Hero("Hanzo", 28, "ninja");
  hero4.attack();
  