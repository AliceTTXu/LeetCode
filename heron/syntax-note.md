## Length

- String: s.length()
- array ex. int[] arr -> arr.length

## Array

- Arrays.sort(arr) // int[] arr
- Copy

```
int[] src  = new int[]{1,2,3,4,5};
int[] dest = new int[5];

System.arraycopy( src, 0, dest, 0, src.length );
```

## Queue

- init: ```Queue<Character> queue = new LinkedList<>();```
- method:
    - ```offer() / poll()```
    - ```size()```

## StringBuilder

- StringBuilder sb = new StringBuilder();
- sb.append(c);

## Char Operations

- Character.isDigit()

## Map

- map.put(d, map.getOrDefault(d, 0) + 1)


```
Collections.sort(people,new Comparator<Person>(){
   @Override
   public int compare(final Person lhs, Person rhs) {
     //TODO return 1 if rhs should be before lhs 
     //     return -1 if lhs should be before rhs
     //     return 0 otherwise
     }
 });
```

```
resultList.toArray(new int[people.length][]);
```

Throws exception	Returns special value
Insert	add(e)	offer(e)
Remove	remove()	poll()
Examine	element()	peek()

Arrays.asList

for (Character c : num.toCharArray()) 
