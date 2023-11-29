import redis, { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
	console.log(`Redis client not connected to the server: ${err.toString()}`)
);
client.on("connect", () => console.log(`Redis client connected to the server`));

export function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

export async function displaySchoolValue(schoolName) {
	console.log(await promisify(client.get.bind(client))(schoolName));
}

async function main() {
	await displaySchoolValue("Holberton");
	setNewSchool("HolbertonSanFrancisco", "100");
	await displaySchoolValue("HolbertonSanFrancisco");
}

main();
