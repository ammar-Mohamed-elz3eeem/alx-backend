import redis, { createClient } from "redis";

const client = createClient();

client.on("error", (err) =>
	console.log(`Redis client not connected to the server: ${err.toString()}`)
);
client.on("connect", () => console.log(`Redis client connected to the server`));

export function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, reply) => {
		redis.print(err, reply);
	});
}

export function displaySchoolValue(schoolName) {
	return client.get(schoolName, (err, reply) => {
		console.log(reply);
	});
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
