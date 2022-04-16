FROM openjdk:8
COPY ./target/SciCal-1.0-SNAPSHOT-jar-with-dependencies.jar ./
WORKDIR ./
# jcdkelws
# java -cp Calculator-0.0.1-SNAPSHOT.jar miniproj.Calculator.App
CMD ["java", "-cp", "Calculator-0.0.1-SNAPSHOT.jar", "miniproj.Calculator.App"]
