"""
Is there an equivalent of C’s ”?:” ternary operator?
Yes, there is. The syntax is as follows:

[on_true] if [expression] else [on_false]

Before this syntax was introduced in Python 2.5, a common idiom was
to use logical operators
До появления этого синтаксиса в Python 2.5 распространенной идиомой было
использование логических операторов

[expression] and [on_true] or [on_false]

However, this idiom is unsafe, as it can give wrong results when on_true has
a false boolean value.
Однако эта идиома небезопасна, поскольку может привести к неверным результатам,
если логическое значение on_true имеет значение false.

Поэтому всегда лучше использовать ... if ... ещё... форму.
Therefore, it is always better to use the

... if ... else ...

form.

"""
x, y = 50, 25
small = x if x < y else y
print(small)

# In these examples, the and expression returns the operand on the left if it
# evaluates to False.
# В этих примерах выражение and возвращает операнд слева, если его значение
# равно False.
#
# Otherwise, it returns the operand on the right.
# В противном случае он возвращает операнд справа.

result = 2 and 3
print(result)

result = 5 and 0.0
print(result)

# With these rules in mind, look again at the code above. In the first
# example, the integer number 2 is true (nonzero), so and returns the right
# operand, 3. In the second example, 5 is true, so and returns the right
# operand even though it evaluates to False.
# Помня об этих правилах, взгляните еще раз на приведенный выше код. В первом
# примере целое число 2 является истинным (ненулевым), поэтому и возвращает
# правильный операнд, 3. Во втором примере значение 5 равно true, поэтому and
# возвращает правильный операнд, даже если его значение равно False.

# The next example uses an empty list ([]) as the left operand. Since empty
# lists evaluate to false, the and expression returns the empty list. The only
# case where you get True or False is the one where you use a Boolean object
# explicitly in the expression.
# В следующем примере в качестве левого операнда используется пустой список
# ([]). Поскольку значение пустых списков равно false, выражение and возвращает
# пустой список. Единственный случай, когда вы получаете значение True или
# False, - это когда вы явно используете логический объект в выражении.
result = [] and 3
print(result)

result = 0 and {}
print(result)


result = 2 or 3
print(result)
# Using the "and" Boolean Operator in Python
# https://realpython.com/python-and-operator/
