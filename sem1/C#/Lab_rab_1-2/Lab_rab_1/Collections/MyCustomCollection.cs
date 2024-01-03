using Lab_rab_1.Interfaces;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_rab_1.Collections
{
    class Node<T>
    {
        public T item;
        public Node<T>? prev;
        public Node<T>? next;
        public Node(T item)
        {
            this.item = item;
            prev = null;
            next = null;
        }
    }
    internal class MyCustomCollection<T> : ICustomCollection<T>, IEnumerable<T>
    {
        int curr_index;
        int size;
        Node<T>? current;
        Node<T>? head;
        Node<T>? tail;

        IEnumerator<T> IEnumerable<T>.GetEnumerator()
        {
            Node<T>? temp = head;
            while(true)
            {
                if(temp == null)
                    yield break;
                yield return temp.item;
                temp = temp.next;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return ((IEnumerable)this).GetEnumerator();
        }

        public MyCustomCollection()
        {
            curr_index = 0;
            size = 0;
            current = null;
            head = null;
            tail = null;
        }

        public void Add(T item)
        {
            size++;
            if(tail == null)
            {
                head = new Node<T>(item);
                current = head;
                tail = head;
                curr_index = 0;
            }
            else
            {
                tail.next = new Node<T>(item);
                tail.next.prev = tail;
                tail = tail.next;
            }
        }

        public T RemoveCurrent()
        {
            if (head == null || tail == null || current == null)
                throw new Exception("Collection Empty");
            else
            {
                T item;
                Node<T>? buf = null;
                int buf_index = curr_index;
                if (current == head)
                {
                    head = head.next;                   
                }
                else if (current == tail)
                {
                    tail = tail.prev;
                }
                else
                {
                    if (current.next != null)
                    {
                        current.next.prev = current.prev;
                        buf = current.next;
                        buf_index = curr_index + 1;
                    }
                    if (current.prev != null)
                    {
                        current.prev.next = current.next;
                        buf = current.prev;
                        buf_index = curr_index - 1;
                    }
                    current.next = null;
                    current.prev = null;
                }
                size--;
                item = current.item;
                current = buf;
                curr_index = buf_index;
                return item;
            }
        }

        public void Remove(T item)
        {
            if (current == null)
                throw new Exception("Collection Empty");
            current = head;
            curr_index = 0;
            while(current != null)
            {
                if (current.item.Equals(item))
                {
                    RemoveCurrent();
                    break;
                }
                current = current.next;
                curr_index++;
            }
            if(current == null)
            {
                current = head;
                curr_index = 0;
                throw new Exception("Item Not Found");
            }
        }

        private void Indexator(int index)
        {
            if (index >= size || index < 0)
                throw new IndexOutOfRangeException();
            if (index > curr_index)
            {
                if (index - curr_index <= size - 1 - index)
                {
                    while (curr_index != index)
                    {
                        curr_index++;
                        current = current?.next;
                    }
                }
                else
                {
                    current = tail;
                    curr_index = size - 1;
                    while (curr_index != index)
                    {
                        curr_index--;
                        current = current?.prev;
                    }
                }
            }
            else
            {
                if (curr_index - index < index)
                {
                    while (curr_index != index)
                    {
                        curr_index--;
                        current = current?.prev;
                    }
                }
                else
                {
                    current = head;
                    curr_index = 0;
                    while (curr_index != index)
                    {
                        curr_index++;
                        current = current?.next;
                    }
                }
            }
        }

        public T this[int index]
        {
            get
            {
                Indexator(index);
                return current.item;
            }
            set
            {
                Indexator(index);
                current.item = value;
            }
        }
        public void Reset()
        {
            current = head;
            curr_index = 0;
        }
        public void Next()
        {
            if (current == null)
                throw new Exception("Collection Empty");
            if (current.next != null)
                current = current.next;
        }
        public void Prev()
        {
            if (current == null)
                throw new Exception("Collection Empty");
            if (current.prev != null)
                current = current.prev;
        }
        public T Current()
        {
            if(current == null)
                throw new Exception("Collection Empty");
            return current.item;
        }

        public int Count
        {
            get
            {
                return size;
            }
        }
    }
}
