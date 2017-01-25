# Python DB API

## SQL Injection
delete all data from DB
The problem with my code is that user input gets put into a database query in an unsafe way

## Curing Bobby Tables

```python
plant = "pumpkin"
c = conn.cursor()
c.execute("insert into garden values(%s)", (plant,))
```

**Never, never, NEVER** user Python string concatenation (+) or string parameters interpolation (%) to pass variables to a SQL query string. Not even at gunpoint.

## Spammy Tables

```javascript
<script>
setTimeout(function() {
    var tt = document.getElementById('content');
    tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
    tt.form.submit();
}, 2500);
</script>
```

![spammy-tables](../lesson3-pic/spammy-tables.png)

## Stopping the spam
[Bleach Documentation](http://bleach.readthedocs.io/en/latest/)

## Updating Away the Spam
```SQL
update table
  set column = value
  where restriction;
```

## Deleting the Spam
```SQL
delete from table
  where restriction;
```
