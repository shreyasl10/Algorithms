var events=require('events');

class Person extends events.EventEmitter{
    constructor(name)
    {
        super();
        this.name=name;
    }
}
var John=new Person('John');
var Joseph=new Person('Joseph');
var Mary=new Person('Mary');
var people=[John,Joseph,Mary];
people.forEach(function(person)
{
    person.on('talk',function(message)
    {
        console.log('Hello this is '+person.name+' speaking.'+message);
    }
    );
}
);
Joseph.emit('talk','I am awesome');
John.emit('talk','I am bored');
Mary.emit('talk','I am lazy');
