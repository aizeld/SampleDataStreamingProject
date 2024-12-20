### Kafka-Spark-Cassandra Data Streaming Project
https://github.com/airscholar/e2e-data-engineering
Этот проект для тех, кто не понимает, почему его проект не работает, даже если он делал всё по видео. Причина может заключаться в несовпадении версий Scala и Spark, устаревших библиотеках или новых версиях инструментов. Более того, оригинальный код из GitHub-репозитория и из видео оказался нерабочим, что подтверждено горьким опытом автора. Этот проект позволяет вам просто запустить и увидеть, как это работает, без ожидания всех деталей из видео.

#### Шаги запуска:

1. **Запустите Docker Compose:**
   Убедитесь, что Docker Compose работает корректно. Все необходимые сервисы (Kafka, Zookeeper, Cassandra и т.д.) поднимутся автоматически.

2. **Создайте виртуальное окружение Python (venv):**
   Лучше делать это на Linux.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Установите зависимости:**
   Установите всё из `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите `kafka_stream.py`:**
   Этот скрипт отвечает за отправку данных в Kafka. Если у вас по каким-то причинам не работает Airflow, запустите альтернативный скрипт `NoDagStream.py`.

5. **Проверьте Kafka:**
   Убедитесь, что сообщения отправляются в топик. Для этого можно использовать Confluent UI или команду CLI Kafka. Проверьте, создан ли топик и поступают ли в него сообщения.

6. **Запустите `spark_stream.py`:**
   Этот скрипт пришлось полностью обновить, так как версия из видео уже не работает. Также код из репозитория GitHub оказался устаревшим. Новый скрипт учитывает все текущие изменения.

7. **Проверьте базу Cassandra:**
   Зайдите прямо в базу Cassandra и проверьте таблицу `created_users`. Если в таблице появились данные, значит проект работает корректно. Например:
   ```cql
   SELECT COUNT(*) FROM spark_streams.created_users;
   ```
   Если видите количество записей, значит всё хорошо.

#### Поздравляем! 🎉
Если вы добрались до этого момента и у вас есть данные в базе Cassandra, вы молодец! Теперь вы понимаете, как работает этот проект. Удачи!

