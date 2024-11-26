#include<iostream>
#include<string>
#include<vector>
#include <iomanip>

    template <typename T> class Item{
    public:
        T name;
        T expiration;
        T category;
        int quantity;
        Item(T n, T e, T c, int q){
            name = n;
            expiration = e;
            category = c;
            quantity = q;
        }
};

    template<typename T> class Inventory{
    public: 
        // write your code
        std::vector<Item<T>> itemsName;
    void addNewItem(const Item<T>& newItem) {
        
        bool present = false;
        for (int i = 0; i < itemsName.size(); i++) {
            if (itemsName[i].name == newItem.name) {
                present = true;
                break;
            }
            
        }
        if (present == true) {
            std::cout << "Item is already present in the inventory" << std::endl;
        }
        else {
            itemsName.push_back(newItem);
        }      
    };
    void increaseQuantity(std::string itemsName, int quantity) {
        
        for (int i = 0; i < itemsName.size(); i++) {
            if (itemsName[i].name == itemsName) {
                itemsName[i].quantity += quantity;
            }
        }

    };

    void updateItem(std::string itemsName, std::string expiration, std::string category, int quantity) {
        for (int i = 0; i < itemsName.size();i++) {
            if (itemsName[i].name == itemsName) {
            itemsName[i].expiration = expiration;
            itemsName[i].quantity = quantity;
            itemsName[i].category = category;   
        }    
        if (itemsName.name != itemsName) {
            throw std::invalid_argument("Item not found");

        }
    }
    };

    void removeItem(std::string itemsName) {
        itemsName.erase(itemsName.begin(), itemsName.end());
        if (itemsName != itemsName) {
            throw std::invalid_argument("Item not found");
        }
    };

    void Total() {
        for (int i = 0; i <= itemsName.size(); i++) {
            std::cout<< "Total number of items in inventory: " << itemsName.quantity[i] << std::endl;
        }
    };

    void searchItem(std::string itemsName) {
        auto it = std::find(itemsName.begin(), itemsName.end()); {
            return itemsName.name == itemsName;
        }
        if (itemsName.name != itemsName) {
            throw std::invalid_argument("Item not found!!");
        }


    };

    void displayItems(){
        std::cout<<"-------Inventory-------"<<std::endl;
        std::cout<<std::left<<std::setw(20)<<"Name"<<std::setw(15)<<"Expiration"<<std::setw
        (15)<<"Quantity"<<std::setw(10)<<"Category"<<std::endl;
        for(int i=0; i<itemsName.size();i++){
            std::cout<<std::left <<
            std::setw(20)<<itemsName[i].name<<std::setw(15)<<itemsName[i].expiration<<std::setw(15)<<
            itemsName[i].quantity<<std::setw(15)<<itemsName[i].category<<std::endl;
        }
    }
};

    template<typename T>class Appointment{
    public:
        T c_name;
        T ap_date;
        T ap_time;
        T CWID;
    Appointment(T n, T d, T t, T cw){
        c_name = n;
        ap_date = d;
        ap_time = t;
        CWID = cw;
        }
};

    template<typename T>
    class AppointmentSystem{
    public:
    // Write Your code
    
    std::vector<Appointment<T>> ap;
    void schedule(const Appointment<T>& newName) {
        std::string n = ap;
        bool present = false;
        for (int i = 0; i < newName.size; i++) {
            if (ap[i].ap == newName.c_name) {
                present = true;
                break;
            }
            
        }
        if (present == true) {
            std::cout << "You already have an appointment " << std::endl;
        }
        else {
            ap.push_back(newName);
        }          
    };

    void Total_appointments(std::string ap_date, std::string ap_time) {
        for (int i = 0; i=ap.size;i++) {
            if (ap[i].name = ap) {
            ap[i].date = ap_date;
            ap[i].time = ap_time;
            int same = ap[i].date + ap[i].time;
            std::cout << "Total Appointments: " << same << std::endl;
            }  
        }
    };    
    
    void removeRecent(){
       if (ap.end()) {
        ap.pop_back();
       }
    };

    void display(){
        std::cout<<"-------Appointments-------"<<std::endl;
        std::cout<<std::left<<std::setw(20)<<"Name"<<std::setw(15)<<"Date"<<std::setw(15)<< "Time"<<std::setw(15)<<"CWID"<<std::endl;
        for(int i=0; i<ap.size();i++){
            std::cout<<std::left <<std::setw(20)<<ap[i].c_name<<std::setw(15)<<ap[i].ap_date<<std::setw(15)<<ap[i].ap_time<<std::setw(15)<<ap[i].CWID<<std::endl;
            }
        }
};
int main() {
// Remove comments and run following test cases
Inventory<std::string> i1;
Item<std::string> I1("Protien Bar","05/09/2023","Snacks",4);
i1.addNewItem(I1);
Item<std::string> I2("Milk","05/12/2023","Regular",2);
i1.addNewItem(I2);
Item<std::string> I3("Cerels","09/12/2023","Snacks",5);
i1.addNewItem(I3);
i1.displayItems();
i1.updateItem("Milk","09/24/2023","Regular",3);
i1.displayItems();
i1.increaseQuantity("Cerels",10);
i1.displayItems();
try{
i1.updateItem("bar","09/12/2023","Snacks",3);
}
catch(const char* msg){
std::cout <<msg << std::endl;
}
i1.displayItems();
i1.updateItem("Cerels","09/27/2023","Regular",4);
i1.displayItems();
i1.Total();
try{
i1.removeItem("Bread");
}
catch(const char* msg){
std::cout<<msg<<std::endl;
}
try{
i1.removeItem("Milk");
}
catch(const char* msg){
std::cout<<msg<<std::endl;
}
i1.displayItems();
try{
i1.searchItem("Cerels");
}
catch(const char* msg){
std::cout<<msg<<std::endl;
}
Appointment<std::string> a1("John Bob","09/12/2023","9:30AM","889456723");
Appointment<std::string> a2("Jim Lee","09/12/2023","10:30AM","883476923");
Appointment<std::string> a3("Chris Lynn","09/12/2023","12:00PM","879455714");
Appointment<std::string> a4("Arnav Shah","09/12/2023","12:00PM","879459583");
AppointmentSystem<std::string> s1;
s1.schedule(a1);
s1.schedule(a2);
s1.schedule(a3);
s1.schedule(a4);
s1.display();
s1.Total_appointments("09/12/2023","12:00PM");
Appointment<std::string> a5("Chris Lynn","09/12/2023","12:00PM","879455714");
s1.schedule(a4);
s1.removeRecent();
s1.display();  
}